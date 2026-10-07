# うたパワー ステージ画像 生成プロンプト集

得点が上がるごとに世界が変わる「ステージ制」用の画像です（目安：1万5千点・3万5千点・6万5千点・10万点で次のステージ。最後のステージはずっと続きます）（タイトルの「みため」で **キラキラ** を選んだときの絵）。
高学年むけの **ライブ** モードの画像は `PROMPTS_LIVE.md` を見てください。
**この文書を Antigravity にそのまま渡して「この通りに画像を作って保存して」と頼めば OK** です。

- 画像が1枚もなくてもアプリは動きます（絵を描いて代わりにしています）。できた分から順に置いていけば、そのぶん豪華になります。
- ステージ1（うちゅう）はいまの見た目のままなので、画像は作らなくて大丈夫です。

## ステージの順番

| # | フォルダ | 名前 | 中心の色 |
|---|---|---|---|
| 1 | `stages/space/` | うちゅうの せかい（いまの見た目） | むらさき・虹色 |
| 2 | `stages/sea/` | うみの せかい | 水色・青 |
| 3 | `stages/flower/` | おはなばたけの せかい | ピンク |
| 4 | `stages/sweets/` | おかしの くに | ピンク・オレンジ・パステル |
| 5 | `stages/sky/` | にじと くもの せかい | 虹色・金色 |

## 1ステージで作るファイル

| ファイル名 | 中身 | サイズ | 備考 |
|---|---|---|---|
| `bg.jpg` | プレイ中の背景 | 16:9（1376×768） | 真ん中に大きな球が乗るので、中央は控えめに |
| `card.jpg` | ステージが変わるときの大きな絵 | 16:9（1376×768） | 下の1/3に文字が乗るので、下は控えめに |
| `orb.png` | 真ん中の大きな球 | 正方形 → 512×512 に縮小 | 丸く切りぬいて使う |
| `ball1.png` `ball2.png` `ball3.png` | 集める玉（順番に使われる） | 正方形 → 256×256 に縮小 | 丸く切りぬいて使う |
| `gold.png` | 10こめの金の玉（ステージクリアの玉） | 正方形 → 256×256 に縮小 | 丸く切りぬいて使う |
| `cutin/1.jpg` 〜 `cutin/4.jpg` | 演出のカットイン | 16:9（1376×768） | いまの `cutin_images/` と同じ雰囲気で |

- **文字は絶対に入れない**でください（ステージ名などはアプリが描きます）。
- 球・玉は**正方形いっぱいに球を描き、背景は真っ黒**にしてください。アプリが円形に切りぬくので、四すみは見えません。jpg で保存しても大丈夫です（その場合 `ball1.jpg` のように拡張子だけ変える）。
- 読み込みを軽くするため、保存のときに縮小・圧縮してください（jpg は品質 80 くらい、1枚 300KB 前後が目安）。

## Antigravity への作業手順

1. 下のプロンプトで画像を作り、上の表のファイル名で `stages/<フォルダ>/` に保存する。
2. 球・玉は縮小する（orb は 512×512、ball・gold は 256×256）。
3. 一覧ファイル `stages/list.json` を作り直す（下のコマンド）。GitHub に push すれば GitHub Actions も自動で作り直すので、忘れても公開ページは大丈夫です。

```bash
python -c "import os,json;d='stages';print(json.dumps({s:sorted(os.path.relpath(os.path.join(r,f),os.path.join(d,s)).replace(os.sep,'/') for r,_,fs in os.walk(os.path.join(d,s)) for f in fs if f.lower().endswith(('.png','.jpg','.jpeg','.webp','.gif'))) for s in sorted(os.listdir(d)) if os.path.isdir(os.path.join(d,s))},ensure_ascii=False,indent=1))" > stages/list.json
```

---

## 共通スタイル（すべてのプロンプトの最初に付ける）

> 絵柄をそろえるため、参考画像として `cutin_images/chii_cutin_pink_diva.jpg` を一緒に渡してください。

```
Style: bright, high-saturation Japanese anime / kawaii game art for elementary school children.
Glossy, glowing neon highlights, clean thick outlines, magical sparkles, cheerful and energetic.
Match the art style of the attached reference image. Absolutely no text, no letters, no numbers, no logos, no UI.
```

## 背景（bg.jpg）共通の指示

```
Game background illustration, 16:9 landscape, 1376x768. Wide establishing view, no characters.
The center of the image must be open and calm (a big glowing sphere will be placed in the center);
put the details mainly around the edges and bottom. Rich colors with deep, slightly dark tones
so that bright glowing effects drawn on top stand out.
```

## ステージ切り替えの絵（card.jpg）共通の指示

```
Stage intro splash illustration for a kids' rhythm game, 16:9 landscape, 1376x768.
Dynamic composition, dramatic burst of light from behind the characters, confetti and sparkles.
Place the characters in the upper 60% of the image; keep the lower third simple and calm
(large title text will be overlaid there). No text.
```

## 球・玉（orb / ball / gold）共通の指示

```
Single game item icon, 1:1 square. One perfectly round sphere seen from the front,
filling the entire square edge to edge (the sphere touches all four edges of the image).
Pure solid black background, no shadow on the ground, no text, no characters.
Glossy surface with a soft white highlight at the upper left.
```

## カットイン（cutin/*.jpg）共通の指示

```
Anime cut-in illustration for a kids' singing game, 16:9 landscape, 1376x768, extremely energetic,
same composition style as the reference: one cute chibi animal in the center in a powerful pose,
radial speed lines, dramatic glow, sparkles, flying music notes. No text.
```

---

## ステージ2　うみの せかい（`stages/sea/`）

**bg.jpg**
```
A magical deep underwater world. Coral reefs in pink, purple and turquoise along the bottom edge,
swaying seaweed at the sides, schools of tiny glowing fish far away, rays of sunlight streaming down
from the surface, floating bubbles. Deep blue gradient getting darker toward the bottom.
```

**card.jpg**
```
A cute chibi dolphin, a little octopus and a baby seal cheerfully welcoming the viewer into
a sparkling underwater kingdom, bubbles bursting all around, beams of light from the surface.
```

**orb.png**
```
A giant iridescent pearl with swirling turquoise water and tiny bubbles visible inside.
```

**ball1.png**
```
A shiny pearl, white with a soft pink and aqua sheen.
```

**ball2.png**
```
A transparent bubble with a rainbow soap-film sheen and a tiny cute fish silhouette inside.
```

**ball3.png**
```
A round turquoise sea-glass marble with a small orange starfish pattern inside.
```

**gold.png**
```
A magnificent golden pearl, shining brightly, with tiny sparkles, like a treasure from a mermaid palace.
```

**cutin/1.jpg**
```
A cute chibi dolphin leaping out of a huge wave, singing with joy, water splashes and bubbles everywhere, blue and aqua glow.
```

**cutin/2.jpg**
```
A cute chibi octopus conducting music with all eight arms, music notes made of bubbles swirling around, purple and pink glow.
```

**cutin/3.jpg**
```
A cute chibi baby seal singing loudly with its eyes closed, a giant bubble ring exploding behind it, white and cyan glow.
```

**cutin/4.jpg**
```
A cute chibi sea turtle surfing on a giant wave with determination, spray and sparkles, turquoise and gold glow.
```

---

## ステージ3　おはなばたけの せかい（`stages/flower/`）

**bg.jpg**
```
A magical flower field at twilight. Rolling hills of tulips, daisies and cosmos in pink, yellow and lavender
along the bottom and sides, giant glowing dandelion puffs, fireflies and floating pollen lights,
a cozy forest of round trees at the far edges, purple-to-pink twilight sky with a few early stars.
```

**card.jpg**
```
A cute chibi bunny, a little bumblebee and a ladybug cheerfully welcoming the viewer into a blooming
flower kingdom, holding flowers, a storm of pink petals swirling around them.
```

**orb.png**
```
A crystal ball containing a tiny blooming pink flower garden with floating petals inside.
```

**ball1.png**
```
A round pink peony flower seen from directly above, filling the whole circle.
```

**ball2.png**
```
A round bright yellow sunflower seen from the front, filling the whole circle.
```

**ball3.png**
```
A round cluster of blue and lavender hydrangea flowers with a few dew drops, filling the whole circle.
```

**gold.png**
```
A golden rose seen from directly above, shining like polished gold, with tiny sparkles.
```

**cutin/1.jpg**
```
A cute chibi bunny jumping high through a storm of flower petals, singing happily, pink and white glow.
```

**cutin/2.jpg**
```
A cute chibi bumblebee singing passionately into a flower like a microphone, golden pollen sparkles, yellow and orange glow.
```

**cutin/3.jpg**
```
A cute chibi ladybug dancing on top of a giant sunflower, petals spinning in a spiral, red and yellow glow.
```

**cutin/4.jpg**
```
A cute chibi squirrel throwing an armful of flower petals into the air with a big smile, green and pink glow.
```

---

## ステージ4　おかしの くに（`stages/sweets/`）

**bg.jpg**
```
A candy kingdom at twilight. Hills of whipped cream and pastel frosting along the bottom, giant lollipop trees
at the sides, a chocolate river, gingerbread houses and a cake castle in the far distance,
candy-cane street lamps glowing warmly, sprinkles floating in the air, pink and purple dusk sky.
```

**card.jpg**
```
A cute chibi teddy bear chef, a hamster hugging a giant donut and a little cupcake fairy cheerfully
welcoming the viewer into a candy kingdom, rainbow sprinkles and candies flying everywhere.
```

**orb.png**
```
A giant round candy ball with swirling pastel pink, mint and cream stripes, like a gumball, glossy like glass.
```

**ball1.png**
```
A round strawberry-pink macaron seen from directly above, filling the whole circle.
```

**ball2.png**
```
A round rainbow swirl lollipop candy seen from the front (no stick visible), filling the whole circle.
```

**ball3.png**
```
A round cookie with white icing and colorful sprinkles seen from directly above, filling the whole circle.
```

**gold.png**
```
A round golden caramel candy wrapped in shining gold, glowing, with tiny sparkles.
```

**cutin/1.jpg**
```
A cute chibi hamster bursting out of a giant strawberry cake, singing with joy, cream and strawberries flying, pink glow.
```

**cutin/2.jpg**
```
A cute chibi teddy bear chef flinging rainbow sprinkles with a big whisk, energetic pose, orange and yellow glow.
```

**cutin/3.jpg**
```
A cute chibi kitten riding a giant spinning lollipop like a wheel, candy swirls around, magenta and mint glow.
```

**cutin/4.jpg**
```
A cute chibi penguin sliding down a chocolate waterfall with arms spread wide, chocolate splashes and candies, brown and gold glow.
```

---

## ステージ5　にじと くもの せかい（`stages/sky/`）

**bg.jpg**
```
Above the clouds at magic hour. A sea of fluffy cotton-candy clouds along the bottom, a huge vivid rainbow
arching across the sky, floating cloud islands with tiny castles at the far sides, golden sunset light
mixing with a violet sky, sparkling stars beginning to appear. A grand, heavenly final-stage feeling.
```

**card.jpg**
```
A cute chibi baby pegasus, a little bluebird and a fluffy cloud sheep cheerfully welcoming the viewer,
riding on a big rainbow above the clouds, golden light rays and sparkles.
```

**orb.png**
```
A crystal ball containing a bright rainbow, fluffy white clouds and a tiny smiling sun inside.
```

**ball1.png**
```
A fluffy round white cloud ball with a soft pastel rainbow glow around its edges.
```

**ball2.png**
```
A round marble with vivid rainbow swirls inside, glossy like glass.
```

**ball3.png**
```
A round bubble of light-blue sky containing a small shining golden star.
```

**gold.png**
```
A golden sun orb with a soft rainbow halo, shining brilliantly, with tiny sparkles.
```

**cutin/1.jpg**
```
A cute chibi baby pegasus flying straight through a rainbow with wings spread wide, rainbow trail, gold and white glow.
```

**cutin/2.jpg**
```
A choir of cute chibi little birds singing together on a fluffy cloud, music notes made of light, sky blue and pink glow.
```

**cutin/3.jpg**
```
A cute chibi fluffy cloud sheep jumping over a rainbow with a joyful face, sparkles and stars, pastel rainbow glow.
```

**cutin/4.jpg**
```
A cute chibi baby dragon happily breathing a rainbow instead of fire, clouds swirling around, rainbow and gold glow.
```

---

## （おまけ）ステージ1 うちゅう も画像にしたいとき（`stages/space/`）

いまの見た目のままで十分ですが、作る場合は同じファイル名で置けば使われます。
`stages/space/cutin/` に置いた場合は、ステージ1のカットインがそちらに切り替わります（置かなければ `cutin_images/` を使います）。
ほかのステージで `cutin/` が空のときも `cutin_images/` が使われます。
