# Crazy City Golf — Press Kit

『Crazy City Golf』のプレスキット。GitHub Pages で公開する。

**公開 URL: https://xz585a.github.io/crazy-city-golf-presskit/**
**Steam: https://store.steampowered.com/app/5347600/**

この URL はすべてのプレスリリースで使い回す。**変えない。**

前作（[prism-factory-presskit](https://github.com/xz585a/prism-factory-presskit)）を写して作った。
何を収録するか・いつ直すかの判断は、ゲーム本体側の `marketing/手順/プレスリリース/プレスキット.md` を正とする。
ここには、このリポジトリの運用だけを書く。

## 言語切り替え

ページ右上のボタンで日本語と英語を切り替える。**本文だけでなく、素材のキャプションや
ボタンのラベルも含めて全体が切り替わる。**

- 初期表示はブラウザの言語設定で決まる（日本語環境なら日本語、それ以外は英語）
- 選んだ言語は `localStorage` に保存され、次回以降そちらで開く
- JS が無効な場合は両言語とも表示される（情報が消えないことを優先）

**テキストを追加するときは、必ず日英の両方を書く。** 片方だけ書くと、その言語では
何も表示されない。マークアップは `class="l-ja"` / `class="l-en"` の対で置く。

```html
<figcaption><span class="l-ja">屋上の近道</span><span class="l-en">Rooftop shortcut</span></figcaption>
```

**切り替わるのは文章だけで、素材は日英で同じものを出す。**トレーラーと GIF は英語 UI の1本ずつで、
言語別に用意しない。**素材のファイル名に言語の接尾辞は付けない。**

## 中身

```text
.
├── index.html          プレスキット本体（日英を1ページに併記）
├── fact_sheet_ja.txt   日本語のファクトシート（配布用テキスト）
├── fact_sheet_en.txt   英語のファクトシート
├── build_thumbs.py     原寸から一覧表示用の縮小版を作る
├── assets/
│   ├── images/         スクリーンショット（原寸 PNG）
│   ├── thumbs/         一覧表示用の縮小版 WebP  ※自動生成。直接編集しない
│   ├── branding/       ロゴ・キーアート・カプセル画像（Steam へ出したものと同じ原寸）、ファビコン
│   ├── gifs/           GIF と、ページ表示用のループ動画（mp4、無音）
│   └── video/          トレーラーの mp4  ※Git 管理外
└── downloads/          一括ダウンロード用の zip  ※Git 管理外
```

**ファイル名は公開URLとして固定しているので変えない。**ゲーム本体側の素材フォルダから
持ち込むときにリネームする。命名は `<番号>_<英語の名前>.<拡張子>`。

**題名の表記に注意する。**文字として出るところは全て `Crazy City Golf`。
`CRAZY CITY GOLF` と全大文字にしない ── 大文字なのは描かれたロゴだけで、それはマークであって語ではない。
**プレスキットの本文は編集部がそのまま記事へ写すので、ここでの表記がそのまま外に出る。**

## 現在の収録物

- GIF **9点**（616×346）と、同じ場面のループ動画（mp4、無音）9点
  - ページ上は mp4 を再生し、GIF はダウンロード用。GIF を9本並べるとページが50MB近くになるため
  - 画面に入ったものだけ再生し、外れたら止める（`index.html` 末尾のスクリプト）
- ロゴ（透過 PNG）、キーアート（ロゴあり・なし）、Steam のカプセル・ライブラリ画像の計10点（`assets/branding/`）
- ファクトシート 日英
- トレーラー（約100秒、29MB に再圧縮した mp4）
- 一括ダウンロード用 zip（65MB。トレーラーは容量の都合で含めない）

### 未収録（決まり次第、足す）

| 何 | 備考 |
| --- | --- |
| スクリーンショット | ゲーム本体側 `marketing/素材/20261002_Steamスクリーンショット/` で選定中。ページには「準備中」と出している |
| 開発者からのひとこと | `index.html` と `fact_sheet_*.txt` の《　》 |
| トレーラーの YouTube 版 | 下記「トレーラー」 |
| 発売時期・価格 | いまは「未定」 |

## 素材の出どころ

| ここ | ゲーム本体側の素材ID・元のファイル |
| --- | --- |
| `assets/gifs/01_meteor_start.gif` 〜 `09_awards.gif` | GIF 一式 `01_同時スタートに隕石_none_16x9_v01.gif` 〜 `09_表彰式_none_16x9_v01.gif`（番号は同じ） |
| `assets/gifs/loop_*.mp4` | 上の GIF を ffmpeg で mp4 にしたもの（下記） |
| `assets/branding/capsule_*`・`keyart_nologo_*` | `20261004_Steamストアカプセル` の `01_heli_hit`（`_logo_` 付きがカプセル、無しがキーアート） |
| `assets/branding/capsule_library_600x900.png`・`library_header_920x430.png`・`hero_3840x1240.png`・`logo_1280x563.png` | `20261002_Steamライブラリ` の採用版 |
| `assets/branding/app_icon.svg` | `20261002_アプリアイコン/app_icon.svg` |
| `assets/video/CrazyCityGolf_Trailer.mp4` | `20261001_steam_promo_90s` の `steam_promo_en_16x9_v20.mp4` |

GIF から mp4 を作り直すとき。

```bash
ffmpeg -i assets/gifs/01_meteor_start.gif -movflags +faststart -pix_fmt yuv420p \
  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -crf 20 -an \
  assets/gifs/loop_01_meteor_start.mp4
```

## 配布アセットの置き場

**zip とトレーラーの mp4 は、リポジトリに入れない。** GitHub Releases の `assets`
タグへ置き、ページからはそこへリンクする。

```text
https://github.com/xz585a/crazy-city-golf-presskit/releases/download/assets/CrazyCityGolf_PressKit.zip
https://github.com/xz585a/crazy-city-golf-presskit/releases/download/assets/CrazyCityGolf_Trailer.mp4
```

理由は、**この2つだけが繰り返し差し替わるうえに大きい**こと。Git はバイナリの差分を
持てないので、作り直すたびに丸ごと履歴へ積み上がり、あとから減らせない。

更新は**同じファイル名で上書き**する。URL が変わらない。

```bash
gh release upload assets downloads/CrazyCityGolf_PressKit.zip --clobber
```

**公開前に、この2つを Releases へ上げておくこと。**ページ上のトレーラーと
一括ダウンロードのリンク先がこの URL なので、上げるまでは 404 になる。

**手元で開いたときだけは、トレーラーが `assets/video/` から再生される。**
`index.html` の末尾に、`localhost` と `file://` でだけ `src` を差し替える数行を入れてある。
Releases がまだ空の状態でも、ページの見え方を確認できる。

```bash
python -m http.server 8765
```

GIF・ループ動画・PNG は Git で管理する。配布物そのもので、差し替えの頻度も低いため。
**ただしコミットするのは公開する確定版だけ**にする（撮り直しの途中経過を入れると、上と同じことが起きる）。

### 画像形式と、原寸／縮小版の分担

配布する原寸は **PNG。**JPEG の圧縮では輪郭や空のグラデーションに滲みが出て、
編集部が記事用に切り出して拡大したときに粗が見える。

原寸を一覧に並べるとページが重くなり、回線の細い環境では開かれずに閉じられる。
そこで**スクリーンショットは表示と配布を分ける。**

| 置き場 | 形式 | 役割 |
| --- | --- | --- |
| `assets/images/` | PNG（原寸） | クリック時のリンク先。zip の中身。**これが配布物** |
| `assets/thumbs/` | WebP（幅960px） | 一覧表示のみ |

縮小版は手で作らない。**スクリーンショットを差し替えたら `build_thumbs.py` を実行する**（Pillow が要る）。

```bash
python build_thumbs.py
```

原寸が消えた分の縮小版は自動で削除される。`assets/thumbs/` を直接編集しない。

## トレーラー

いまはページに `<video>` を置き、Releases の mp4 を直接再生している。
元素材（約100秒、498MB）を ffmpeg で 29MB へ再圧縮したものである。

```bash
ffmpeg -i steam_promo_en_16x9_v20.mp4 -c:v libx264 -preset slow -crf 24 \
  -maxrate 2200k -bufsize 4400k -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 128k assets/video/CrazyCityGolf_Trailer.mp4
```

**YouTube へ上げたら、`#trailer` セクションの `<video>` を
`youtube-nocookie.com/embed/<id>` の iframe へ差し替える**（`class="trailer-player"` は
そのまま使う）。mp4 のダウンロードリンクは残す ── 編集部が使う。ファクトシートのトレーラー欄も同時に直す。

**iframe にもインライン `style` で `display` を書かないこと。** 言語切り替えの
`display:none` に勝ってしまう。高さは `.trailer-player` の `aspect-ratio: 16 / 9` が
担っている（iframe には固有の縦横比がないため、これを外すと潰れる）。

**記事に載ったあとは、古いトレーラーを YouTube から消さない。**記事側の埋め込みが死ぬ。限定公開で残す。

## zip の作り直し

素材を追加・差し替えたら zip も作り直し、**Releases へ上書きアップロードする**。
zip 自体はコミットされない。容量が変わったら `index.html` のボタンの表記も直す。

```bash
python - <<'EOF'
import os
import zipfile

out = "downloads/CrazyCityGolf_PressKit.zip"
os.path.exists(out) and os.remove(out)
z = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
for f in ["fact_sheet_ja.txt", "fact_sheet_en.txt"]:
    z.write(f, "CrazyCityGolf_PressKit/" + f)
for sub in ["assets/images", "assets/gifs", "assets/branding"]:
    for f in sorted(os.listdir(sub)):
        if not f.startswith("."):
            z.write(os.path.join(sub, f), "CrazyCityGolf_PressKit/" + sub.split("/")[1] + "/" + f)
z.close()
EOF
gh release upload assets downloads/CrazyCityGolf_PressKit.zip --clobber
```

## 素材を追加したときの手順

1. スクリーンショットは `assets/images/`（原寸）へ置く。命名は `<番号>_<名前>.png`
2. `python build_thumbs.py` を実行して縮小版を作り直す
3. `index.html` の対応する grid に `<figure>` を足す（`figcaption` は日英の対で書く）
4. zip を作り直し、Releases へ上書きアップロードする
5. コミットして push する。GitHub Pages への反映は数十秒〜数分

## 公開の手順（初回）

```bash
gh repo create crazy-city-golf-presskit --public --source . --remote origin --push
```

push したら、リポジトリの Settings → Pages で **Source を `Deploy from a branch`、
Branch を `main` / `(root)`** にする。数十秒で
`https://xz585a.github.io/crazy-city-golf-presskit/` が開く。

その後、上の「配布アセットの置き場」のコマンドで zip とトレーラーを Releases へ上げる。

```bash
gh release create assets --title assets --notes "press kit assets" || true
gh release upload assets assets/video/CrazyCityGolf_Trailer.mp4 --clobber
gh release upload assets downloads/CrazyCityGolf_PressKit.zip --clobber
```

## 制約

- **1ファイル 100MB まで**（Releases 側は 2GB まで）。ページに直接置く mp4 は
  20〜30MB に収め、原寸は Releases か YouTube へ逃がす
- サイト全体で 1GB まで
- **このリポジトリはパブリック。** 未公開の情報を含むファイルを置かない
