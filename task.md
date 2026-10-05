# うたパワー ステージ画像生成タスク

## 進捗概要
- [x] 各ステージ用フォルダの作成 (`sea/cutin`, `flower/cutin`, `sweets/cutin`, `sky/cutin`)
- [x] 画像後処理・list.json更新スクリプトの作成 (`process_stages.py`)
- [x] ステージ2: うみの せかい (`stages/sea/`) - 全11枚完了
  - bg.jpg, card.jpg, orb.png, ball1.png, ball2.png, ball3.png, gold.png, cutin/1.jpg 〜 4.jpg
- [x] ステージ3: おはなばたけの せかい (`stages/flower/`) - 全11枚完了
  - bg.jpg, card.jpg, orb.png, ball1.png, ball2.png, ball3.png, gold.png, cutin/1.jpg 〜 4.jpg
- [ ] ステージ4: おかしの くに (`stages/sweets/`) - 一部完了 (bg.jpg, card.jpg, orb.png, ball1.png)
  - 未生成: ball2.png, ball3.png, gold.png, cutin/1.jpg 〜 4.jpg
- [ ] ステージ5: にじと くもの せかい (`stages/sky/`)
- [x] 生成済み画像の縮小・圧縮・配置 (球 512x512, 玉 256x256, JPEG圧縮)
- [x] `stages/list.json` の更新 (sea: 11枚, flower: 11枚, sweets: 4枚反映済み)
- [!] 画像生成APIクォータ制限発生 (`gemini-3.1-flash-image` 429 Too Many Requests, 次回リセット予定: 日本時間 18:36 頃 / 残り約4時間27分)
