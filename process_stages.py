"""
うたパワー ステージ画像の後処理スクリプト (process_stages.py)

機能:
1. stages/ 配下の球・玉画像を適切なサイズに縮小
   - orb: 512x512
   - ball1, ball2, ball3, gold: 256x256
2. 各画像をWeb向けに軽量化 (JPEG品質 80-85, 最適化)
3. stages/list.json を再生成
"""

import os
import json
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
STAGES_DIR = BASE_DIR / "stages"

RESIZE_RULES = {
    "orb": (512, 512),
    "ball1": (256, 256),
    "ball2": (256, 256),
    "ball3": (256, 256),
    "gold": (256, 256),
}

def process_images():
    if not STAGES_DIR.exists():
        print(f"Error: {STAGES_DIR} not found")
        return

    stages = [d for d in STAGES_DIR.iterdir() if d.is_dir()]
    print(f"Found {len(stages)} stage directories: {[s.name for s in stages]}")

    for stage in sorted(stages):
        for img_path in stage.rglob("*"):
            if not img_path.is_file():
                continue
            ext = img_path.suffix.lower()
            if ext not in [".png", ".jpg", ".jpeg", ".webp"]:
                continue

            stem = img_path.stem.lower()

            # リサイズ判定
            target_size = RESIZE_RULES.get(stem)
            try:
                with Image.open(img_path) as im:
                    orig_size = im.size
                    if target_size and orig_size != target_size:
                        print(f"[{stage.name}] Resizing {img_path.name} from {orig_size} to {target_size}...")
                        im = im.resize(target_size, Image.Resampling.LANCZOS)
                        im.save(img_path, optimize=True)
                    elif ext in [".jpg", ".jpeg"]:
                        # JPEG 圧縮の最適化（1MBを超えるような巨大ファイルを適正化）
                        file_size_kb = img_path.stat().st_size / 1024
                        if file_size_kb > 500:
                            print(f"[{stage.name}] Compressing {img_path.name} ({file_size_kb:.1f} KB)...")
                            im.save(img_path, quality=82, optimize=True)
            except Exception as e:
                print(f"Error processing {img_path}: {e}")

    update_list_json()

def update_list_json():
    result = {}
    for stage_dir in sorted(STAGES_DIR.iterdir()):
        if not stage_dir.is_dir():
            continue
        rel_files = []
        for root, _, files in os.walk(stage_dir):
            for f in files:
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, stage_dir).replace(os.sep, '/')
                    rel_files.append(rel_p)
        result[stage_dir.name] = sorted(rel_files)

    list_json_path = STAGES_DIR / "list.json"
    with open(list_json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print(f"Updated {list_json_path}")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    process_images()
