# うたパワー ステージ画像生成タスク

## 進捗概要
- [x] 各ステージ用フォルダの作成 (`sea/cutin`, `flower/cutin`, `sweets/cutin`, `sky/cutin`)
- [x] 画像後処理・list.json更新スクリプトの作成 (`process_stages.py`)
- [x] ステージ2: うみの せかい (`stages/sea/`) - 全11枚完了
  - bg.jpg, card.jpg, orb.png, ball1.png, ball2.png, ball3.png, gold.png, cutin/1.jpg 〜 4.jpg
- [x] ステージ3: おはなばたけの せかい (`stages/flower/`) - 全11枚完了
  - bg.jpg, card.jpg, orb.png, ball1.png, ball2.png, ball3.png, gold.png, cutin/1.jpg 〜 4.jpg
- [x] ステージ4: おかしの くに (`stages/sweets/`) - 全11枚完了
  - bg.jpg, card.jpg, orb.png, ball1.png, ball2.png, ball3.png, gold.png, cutin/1.jpg 〜 4.jpg
- [x] ステージ5: にじと くもの せかい (`stages/sky/`) - 全11枚完了
  - bg.jpg, card.jpg, orb.png, ball1.png, ball2.png, ball3.png, gold.png, cutin/1.jpg 〜 4.jpg
- [x] 全画像の縮小・圧縮・配置 (球 512x512, 玉 256x256, Web最適化JPEG圧縮)
- [x] `stages/list.json` の更新 (sea: 11枚, flower: 11枚, sweets: 11枚, sky: 11枚 / 全44枚完了)
- [x] 全ステージ画像生成タスク 100% 完了！

---

# 「ライブ」モード（高学年むけ）画像生成タスク　→ `stages/PROMPTS_LIVE.md`

- [ ] さいしょに `stages/street/cutin/1.jpg`（ソラ）を作り、絵柄の見本にする
- [ ] ステージ1: よるの ストリート (`stages/street/`) 0/11
- [ ] ステージ2: ちかの ライブハウス (`stages/livehouse/`) 0/11
- [ ] ステージ3: ゆうやけ アリーナ (`stages/arena/`) 0/11
- [ ] ステージ4: きょだい ドーム (`stages/dome/`) 0/11
- [ ] ステージ5: うちゅう フェス (`stages/galaxy/`) 0/11
- [ ] `python process_stages.py` で縮小・圧縮と list.json の更新
