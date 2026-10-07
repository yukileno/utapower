"""
ImageFX（ブラウザの画像生成）で「ライブ」モードの画像を作るための お手伝いスクリプト

使い方:
    python imagefx.py              まだ無い画像を 順番に作る
    python imagefx.py street/bg    1枚だけ 作り直す（すでにあっても上書き）

1. 次に作る画像のプロンプトが クリップボードに コピーされる
2. ImageFX に 貼りつけて 生成し、気に入った1枚を ダウンロードする
3. ダウンロードフォルダに 画像が来たら、縮小して stages/<ステージ>/ に 正しい名前で 置き、次へ進む
   （待っている間に s で とばす、q で おわる）

プロンプトは stages/PROMPTS_LIVE.md から 組み立てる。文書を直せば プロンプトも変わる
"""

import json
import msvcrt
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image, ImageOps

BASE_DIR = Path(__file__).resolve().parent
STAGES_DIR = BASE_DIR / "stages"
DOC = STAGES_DIR / "PROMPTS_LIVE.md"
DOWNLOADS = Path.home() / "Downloads"

STAGES = ["street", "livehouse", "arena", "dome", "galaxy"]
NAMES = ["bg", "card", "orb", "ball1", "ball2", "ball3", "gold",
         "cutin/1", "cutin/2", "cutin/3", "cutin/4"]
CUT_CHARS = {"cutin/1": "SORA", "cutin/2": "AKANE", "cutin/3": "RUI", "cutin/4": "MITSUKI"}
ROUND = {"orb": 512, "ball1": 256, "ball2": 256, "ball3": 256, "gold": 256}
WIDE = (1376, 768)
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp")


def load_doc():
    """文書から 共通の指示と、ステージごとの プロンプトを 取り出す"""
    text = DOC.read_text(encoding="utf-8")
    sections = re.split(r"^## ", text, flags=re.M)

    def block(head):
        for s in sections:
            if s.startswith(head):
                m = re.search(r"```\n(.*?)```", s, re.S)
                return m.group(1).strip()
        raise SystemExit(f"{DOC.name} に「{head}」の ``` ブロックが 見つからない")

    common = {
        "style": block("共通スタイル"),
        "chars": block("キャラクター設定"),
        "bg": block("背景（bg.jpg）"),
        "card": block("ステージ切り替えの絵"),
        "round": block("球・玉"),
        "cutin": block("カットイン（cutin"),
    }
    per = {}
    for s in sections:
        m = re.search(r"`stages/(\w+)/`", s.splitlines()[0]) if s.strip() else None
        if not m:
            continue
        stage = m.group(1)
        items = {}
        # **bg.jpg**\n```...```  と  **cutin/1.jpg** `...` の 2つの書き方
        for name, body in re.findall(r"\*\*([\w/]+)\.(?:jpg|png)\*\*\s*\n```\n(.*?)```", s, re.S):
            items[name] = body.strip()
        for name, body in re.findall(r"\*\*([\w/]+)\.(?:jpg|png)\*\*\s*`([^`]+)`", s):
            items[name] = body.strip()
        per[stage] = items
    return common, per


def build_prompt(common, per, stage, name):
    own = per.get(stage, {}).get(name)
    if not own:
        raise SystemExit(f"{DOC.name} に {stage}/{name} の プロンプトが 無い")
    parts = [common["style"]]
    if name == "bg":
        parts += [common["bg"]]
    elif name == "card":
        parts += [common["chars"], common["card"]]
    elif name in ROUND:
        parts += [common["round"]]
    else:
        # カットインは その回の キャラだけ 説明する（ほかのキャラが まざらないように）
        who = CUT_CHARS[name]
        chars = "\n".join(l for l in common["chars"].splitlines() if not l.startswith("- ") or l.startswith(f"- {who}:"))
        parts += [chars, common["cutin"]]
    parts.append(own)
    return "\n\n".join(parts)


def target_path(stage, name):
    ext = ".png" if name in ROUND else ".jpg"
    return STAGES_DIR / stage / (name + ext)


def exists(stage, name):
    d = STAGES_DIR / stage
    return any((d / (name + e)).exists() for e in IMG_EXT)


def copy_to_clipboard(text):
    subprocess.run("clip", input=text.encode("utf-16"), check=True)


def wait_download(since):
    """ダウンロードフォルダに 新しい画像が来るまで待つ。s=とばす q=おわる"""
    while True:
        while msvcrt.kbhit():
            k = msvcrt.getwch().lower()
            if k in ("s", "q"):
                return k
        for p in DOWNLOADS.iterdir():
            if p.suffix.lower() in IMG_EXT and p.stat().st_mtime > since:
                time.sleep(0.8)  # 書きこみが おわるのを 待つ
                return p
        time.sleep(0.5)


def save_image(src, stage, name):
    out = target_path(stage, name)
    out.parent.mkdir(parents=True, exist_ok=True)
    # 同じ名前で 拡張子ちがいの 古いファイルは 消す（list.json に 2つ のらないように）
    for e in IMG_EXT:
        old = out.with_suffix(e)
        if old != out and old.exists():
            old.unlink()
    with Image.open(src) as im:
        im = im.convert("RGB")
        if name in ROUND:
            n = ROUND[name]
            ImageOps.fit(im, (n, n), Image.Resampling.LANCZOS).save(out, optimize=True)
        else:
            ImageOps.fit(im, WIDE, Image.Resampling.LANCZOS).save(out, quality=82, optimize=True)
    return out


def update_list_json():
    result = {}
    for d in sorted(p for p in STAGES_DIR.iterdir() if p.is_dir()):
        result[d.name] = sorted(p.relative_to(d).as_posix() for p in d.rglob("*")
                                if p.suffix.lower() in IMG_EXT + (".gif",))
    (STAGES_DIR / "list.json").write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main():
    common, per = load_doc()
    if len(sys.argv) > 1:
        stage, name = sys.argv[1].split("/", 1)
        todo = [(stage, name)]
    else:
        # 絵柄の見本になる ソラの カットインを いちばん さいしょに
        order = [("street", "cutin/1")] + [(s, n) for s in STAGES for n in NAMES if (s, n) != ("street", "cutin/1")]
        todo = [(s, n) for s, n in order if not exists(s, n)]
    if not todo:
        print("ぜんぶ そろっています！")
        return

    print(f"ImageFX を ブラウザで ひらいておいてね。のこり {len(todo)} 枚\n")
    for i, (stage, name) in enumerate(todo, 1):
        prompt = build_prompt(common, per, stage, name)
        copy_to_clipboard(prompt)
        shape = "正方形（1:1）" if name in ROUND else "横長（16:9）"
        print(f"[{i}/{len(todo)}] {stage}/{name}  … 形は {shape}")
        print("  プロンプトを コピーしました。ImageFX に 貼りつけて 生成 → 気に入った1枚を ダウンロード")
        if (stage, name) == ("street", "cutin/1"):
            print("  ※ これが 絵柄の 見本になります。気に入るまで 何回でも 作り直してね")
        print("  （s = とばす、q = おわる）")
        got = wait_download(time.time())
        if got == "q":
            break
        if got == "s":
            print("  とばしました\n")
            continue
        out = save_image(got, stage, name)
        got.unlink()  # ダウンロードフォルダに たまらないように
        print(f"  → {out.relative_to(BASE_DIR)} に おきました\n")
        update_list_json()
    update_list_json()
    print("おわり。git で コミット＆プッシュすると 公開ページに 出ます")


if __name__ == "__main__":
    main()
