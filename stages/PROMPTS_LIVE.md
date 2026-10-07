# うたパワー「ライブ」モード 画像 生成プロンプト集

タイトル画面の「みため」で **ライブ** を選んだときの画像です（高学年むけ・かっこいい系）。
「キラキラ」モード（いままでの絵）は `PROMPTS.md` のまま、さわりません。

**この文書を Antigravity にそのまま渡して「この通りに画像を作って保存して」と頼めば OK** です。

- 画像が1枚もなくてもアプリは動きます（照明やレーザーを描いて代わりにしています）。できた分から順に置いていけば、そのぶん豪華になります。
- 子ども向けなので、**コイン・スロット・サイコロ・トランプ・「777」など、ギャンブルを連想させるものは絵に入れない**でください。

## ステージの順番（歌うほど会場が大きくなる「ライブツアー」）

| # | フォルダ | 名前 | 中心の色 |
|---|---|---|---|
| 1 | `stages/street/` | よるの ストリート | マゼンタ・シアンのネオン |
| 2 | `stages/livehouse/` | ちかの ライブハウス | 赤・白のスポットライト |
| 3 | `stages/arena/` | ゆうやけ アリーナ | オレンジ・金・花火 |
| 4 | `stages/dome/` | きょだい ドーム | 青・緑・紫のレーザー |
| 5 | `stages/galaxy/` | うちゅう フェス | 金・虹色・星空 |

## 1ステージで作るファイル（PROMPTS.md と同じ）

| ファイル名 | 中身 | サイズ | 備考 |
|---|---|---|---|
| `bg.jpg` | プレイ中の背景 | 16:9（1376×768） | 真ん中に大きな球が乗るので、中央は控えめに |
| `card.jpg` | ステージが変わるときの大きな絵 | 16:9（1376×768） | 下の1/3に文字が乗るので、下は控えめに |
| `orb.png` | 真ん中の大きな球 | 正方形 → 512×512 に縮小 | 丸く切りぬいて使う |
| `ball1.png` `ball2.png` `ball3.png` | 集める玉 | 正方形 → 256×256 に縮小 | 丸く切りぬいて使う |
| `gold.png` | 10こめの金の玉 | 正方形 → 256×256 に縮小 | 丸く切りぬいて使う |
| `cutin/1.jpg` 〜 `cutin/4.jpg` | 演出のカットイン | 16:9（1376×768） | 1=ソラ 2=アカネ 3=ルイ 4=ミツキ |

- **文字は絶対に入れない**（ステージ名などはアプリが描きます）。
- 球・玉は**正方形いっぱいに球を描き、背景は真っ黒**。jpg でも OK（`ball1.jpg` のように拡張子だけ変える）。
- 保存後に `python process_stages.py` を実行すると、縮小・圧縮と `stages/list.json` の作り直しをまとめてやってくれます。

## 作る順番（絵柄をそろえるコツ）

1. **いちばん最初に `stages/street/cutin/1.jpg`（ソラ）を作る。** これが絵柄の見本になります。
2. 気に入ったら、それ以降の **すべての画像に参考画像として `stages/street/cutin/1.jpg` を一緒に渡す**。
3. キャラが出る絵（card・cutin）は、下の「キャラクター設定」の説明を毎回そのまま付ける。

---

## 共通スタイル（すべてのプロンプトの最初に付ける）

```
Style: cool, stylish Japanese anime game key art for upper elementary / middle school kids (ages 10-14),
like a modern rhythm game or music anime. Sleek proportions (normal head-to-body ratio, NOT chibi, NOT kawaii, NOT babyish),
confident expressions, sharp clean lineart, cinematic lighting with strong rim light, high contrast,
dark backgrounds lit by vivid neon and stage lights, lens flares, light particles.
Absolutely no text, no letters, no numbers, no logos, no UI. No coins, no slot machines, no dice, no playing cards.
```

## キャラクター設定（card・cutin に毎回付ける）

4人組のオリジナル音楽ユニット。全員 13〜14 歳くらい。

```
Characters (original, keep their designs consistent):
- SORA: boy, messy black hair with a single cyan streak, sharp blue eyes, white hoodie under a black cropped jacket, headphones around his neck, holds a microphone. Theme color: cyan.
- AKANE: girl, long red-orange high ponytail, confident amber eyes, black jacket with red lines, fingerless gloves, holds a microphone. Theme color: red.
- RUI: boy, silver hair covering one eye, calm violet eyes, long dark-purple coat, plays a glowing keytar. Theme color: purple.
- MITSUKI: girl, short navy-blue bob with a gold hairpin, energetic grin, oversized yellow-and-black jacket, twirls glowing drumsticks. Theme color: gold.
```

## 背景（bg.jpg）共通の指示

```
Game background illustration, 16:9 landscape, 1376x768. Wide establishing view of the venue, no characters (a crowd silhouette is OK).
The center of the image must be open and dark (a big glowing sphere will be placed in the center);
put the details mainly around the edges and bottom. Deep, dark tones so that bright glowing effects drawn on top stand out.
```

## ステージ切り替えの絵（card.jpg）共通の指示

```
Stage intro splash illustration for a rhythm game, 16:9 landscape, 1376x768.
All four characters (SORA, AKANE, RUI, MITSUKI) performing together on the stage, dynamic low-angle shot,
dramatic backlight burst behind them. Place the characters in the upper 60% of the image;
keep the lower third darker and simple (large title text will be overlaid there). No text.
```

## 球・玉（orb / ball / gold）共通の指示

```
Single game item icon, 1:1 square. One perfectly round sphere seen from the front,
filling the entire square edge to edge (the sphere touches all four edges of the image).
Pure solid black background, no shadow on the ground, no text, no characters.
Glossy, high-tech look with a sharp white highlight at the upper left and a glowing core.
```

## カットイン（cutin/*.jpg）共通の指示

```
Anime cut-in illustration for a rhythm game, 16:9 landscape, 1376x768, extremely energetic and cool.
One character in a dynamic close-up power pose (waist-up or face close-up), diagonal composition,
radial speed lines, dramatic glow in the character's theme color, light particles and glowing sound waves. No text.
```

カットインは各ステージ共通で **1=SORA（マイクを突き出して歌う）2=AKANE（マイクを持ってシャウト）3=RUI（キーターを弾く）4=MITSUKI（ドラムスティックをかかげる）**。
下の各ステージのカットイン文は「その会場らしさ」を足すためのものです。

---

## ステージ1　よるの ストリート（`stages/street/`）

**bg.jpg**
```
A Japanese city street at night after rain. Neon signs without readable text in magenta, cyan and purple along both sides,
wet asphalt reflecting the neon, a small street-performance spot with a single amp and mic stand at the bottom,
a few silhouettes of people gathering, skyscrapers fading into the dark sky.
```

**card.jpg**
```
The four characters doing a guerrilla street live at night, standing on a small corner stage of crates,
neon city behind them, a growing crowd of silhouettes with phone lights raised, magenta and cyan light.
```

**orb.png**
```
A dark glass sphere with swirling magenta and cyan neon light trails inside, like a city at night seen through a lens.
```

**ball1.png**
```
A glossy magenta neon sphere with a glowing ring of light around its equator.
```

**ball2.png**
```
A cyan glass sphere with a glowing sound-wave line running across the inside.
```

**ball3.png**
```
A deep purple sphere with tiny city lights (bokeh) sparkling inside.
```

**gold.png**
```
A brilliant golden sphere with a glowing neon-white music note engraved in the center, shining with light rays.
```

**cutin/1.jpg** `SORA singing hard into the mic on a rainy neon street, neon reflections, cyan glow.`
**cutin/2.jpg** `AKANE shouting into the mic with her ponytail flying, neon signs blurred behind her, red and magenta glow.`
**cutin/3.jpg** `RUI playing the keytar under a streetlight, glowing sound waves spreading through the night city, purple glow.`
**cutin/4.jpg** `MITSUKI jumping with drumsticks raised high above a crowd of phone lights, gold and magenta glow.`

---

## ステージ2　ちかの ライブハウス（`stages/livehouse/`）

**bg.jpg**
```
A small underground live house seen from the floor. Black walls, a low stage with amps and a drum kit at the bottom,
strong white and red spotlights cutting through haze from the ceiling at the edges, a packed crowd silhouette raising hands at the bottom edge.
```

**card.jpg**
```
The four characters exploding into the first song on a cramped live-house stage, red and white spotlights,
haze, the crowd jumping, sweat and energy, sparks of light.
```

**orb.png**
```
A dark sphere like a stage spotlight lens, with a bright white-hot core and red light beams radiating inside.
```

**ball1.png**
```
A glossy red sphere with a white spotlight reflection and smoky haze inside.
```

**ball2.png**
```
A round speaker cone seen from the front, black with a glowing red rim, filling the whole circle.
```

**ball3.png**
```
An orange-gold glass sphere with a tiny glowing guitar-pick-shaped light inside.
```

**gold.png**
```
A shining golden sphere with a red flame-like aura, like a trophy of the first sold-out live.
```

**cutin/1.jpg** `SORA singing with one foot on a monitor speaker, red spotlight from above, haze, cyan and red glow.`
**cutin/2.jpg** `AKANE screaming into the mic, hair whipping, white strobe light behind her, red glow.`
**cutin/3.jpg** `RUI's fingers flying over the keytar keys, close-up, red and purple stage lights, sound waves.`
**cutin/4.jpg** `MITSUKI hitting the drums with full force, cymbals flashing, light sparks flying, gold and red glow.`

---

## ステージ3　ゆうやけ アリーナ（`stages/arena/`）

**bg.jpg**
```
A huge open-air arena at sunset. Orange and violet sky, fireworks starting to burst at the top corners,
a giant stage with light towers at the bottom, a sea of thousands of glowing penlights in the crowd along the bottom edge.
```

**card.jpg**
```
The four characters on a giant arena stage at sunset, fireworks bursting behind them, golden confetti,
tens of thousands of penlights glowing in the crowd, orange and gold light.
```

**orb.png**
```
A crystal sphere containing a sunset sky with fireworks bursting inside.
```

**ball1.png**
```
A glowing orange sphere like a setting sun, with a soft light flare.
```

**ball2.png**
```
A sphere made of a firework burst frozen in glass, gold and red sparks inside.
```

**ball3.png**
```
A violet glass sphere with dozens of tiny penlight dots glowing inside like a crowd.
```

**gold.png**
```
A magnificent golden sphere bursting with firework sparks, shining brilliantly.
```

**cutin/1.jpg** `SORA reaching his hand toward the crowd while singing, sunset and fireworks behind him, cyan and orange glow.`
**cutin/2.jpg** `AKANE on the edge of the stage pointing at the sky, a firework exploding behind her, red and gold glow.`
**cutin/3.jpg** `RUI playing the keytar with confetti raining down, sunset backlight, purple and orange glow.`
**cutin/4.jpg** `MITSUKI throwing a drumstick spinning into the air, golden fireworks, gold glow.`

---

## ステージ4　きょだい ドーム（`stages/dome/`）

**bg.jpg**
```
Inside a gigantic dome stadium during a concert. Dark ceiling, dozens of laser beams in cyan, green and purple
shooting from the stage at the bottom, huge LED screens (showing only abstract light, no text) at the sides,
a vast ocean of blue penlights filling the bottom.
```

**card.jpg**
```
The four characters rising up on a lift in the center of a massive dome stage, laser beams in every direction,
pillars of fire and light, fifty thousand penlights, cyan, green and purple light.
```

**orb.png**
```
A dark sphere with a grid of glowing cyan laser lines inside, like a high-tech energy core.
```

**ball1.png**
```
A cyan energy core sphere with glowing circuit lines.
```

**ball2.png**
```
A green glass sphere crossed by thin laser beams of light.
```

**ball3.png**
```
A deep blue sphere with a purple glowing ring orbiting around it.
```

**gold.png**
```
A golden energy core sphere with radiating laser beams of light, shining brilliantly.
```

**cutin/1.jpg** `SORA singing with his eyes closed under crossing laser beams, cyan glow.`
**cutin/2.jpg** `AKANE striking a pose as pillars of fire erupt behind her, red and orange glow.`
**cutin/3.jpg** `RUI playing the keytar with green lasers fanning out behind him, purple and green glow.`
**cutin/4.jpg** `MITSUKI drumming as a giant shockwave of light spreads across the dome, gold and cyan glow.`

---

## ステージ5　うちゅう フェス（`stages/galaxy/`）

**bg.jpg**
```
A legendary music festival stage floating in outer space. A glowing stage platform on an asteroid at the bottom,
a spiral galaxy and colorful nebulae in the sky, light beams shooting up into space at the edges,
tiny glowing lights of an audience on floating islands. A grand, final-stage feeling.
```

**card.jpg**
```
The four characters performing on a stage floating in space, a huge galaxy behind them,
beams of rainbow light shooting into the stars, planets and nebulae, gold and rainbow light.
```

**orb.png**
```
A crystal sphere containing a swirling spiral galaxy with a glowing core.
```

**ball1.png**
```
A small planet sphere with glowing cyan rings.
```

**ball2.png**
```
A magenta nebula swirling inside a glass sphere, with tiny stars.
```

**ball3.png**
```
A shining white-blue star sphere with a soft light halo.
```

**gold.png**
```
A golden sun-like star sphere with a rainbow halo, shining brilliantly, the ultimate prize.
```

**cutin/1.jpg** `SORA singing toward the stars, a galaxy swirling behind him, cyan and gold glow.`
**cutin/2.jpg** `AKANE with her hand raised, a comet streaking past behind her, red and gold glow.`
**cutin/3.jpg** `RUI playing the keytar as sound waves turn into rings of stars, purple glow.`
**cutin/4.jpg** `MITSUKI hitting the final beat as a supernova of light explodes behind her, gold and rainbow glow.`
