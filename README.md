# Crazy City Golf — Press Kit

『Crazy City Golf』のプレスキット。GitHub Pages で公開する。

**公開 URL: https://xz585a.github.io/crazy-city-golf-presskit/**
**Steam: https://store.steampowered.com/app/5347600/**

この URL はすべてのプレスリリースで使い回す。**変えない。**

前作（[prism-factory-presskit](https://github.com/xz585a/prism-factory-presskit)）を写して作った。
何を収録するか・いつ直すかの判断は、ゲーム本体側の `marketing/手順/プレスリリース/プレスキット.md` を正とする。
ここには、このリポジトリの運用だけを書く。

## 状態（2026-10-08）

- **内容は一旦完成。未公開。**このフォルダ（`C:\Godot\crazy-city-golf-presskit`）にだけあり、GitHub にはまだ無い
- 公開するときは下の「公開の手順（初回）」を上から行う
- 残っているもの：開発者のひとこと（《　》）、スクリーンショットの原寸、トレーラーの YouTube 版、発売時期・価格

**GitHub へ上げるまで、ここが唯一のコピーである。**PC の移行や掃除の前に公開するか、別の場所へ複製する。
`assets/video/` と `downloads/` は Git に入らないが、どちらも下の手順で作り直せる。

## 編集のしかた

**`index.html` を直接編集する。**ページを生成する仕組みは無い。手元で見るときはこのフォルダで

```bash
python -m http.server 8765
```

を実行し、<http://localhost:8765/> を開く（トレーラーも手元のファイルで再生される）。

### 同じ内容が書いてある場所

文章を直すときは、次の**4か所を必ずそろえる。**記者はページとファクトシートのどちらを引用するか分からない。

| 内容 | `index.html` | ファクトシート |
| --- | --- | --- |
| 概要・特徴・製品情報・開発者 | `<!-- 日本語 -->` と `<!-- English -->` の2ブロック（`#about`） | `fact_sheet_ja.txt` / `fact_sheet_en.txt` |
| 連絡先 | `#contact` の日英2つの表 | 両ファイルの末尾 |
| 一行紹介 | `<header>` の `tagline` 2つ | （なし） |
| 素材の利用許諾 | `#downloads` の日英 | 両ファイル |

ゲーム本体側のストア説明文やプレスリリースの文面とも、主張をそろえる。

### よくある編集

| やりたいこと | 直す所 |
| --- | --- |
| 開発者のひとことを入れる | `index.html` の《開発者からのひとこと…》と《A few lines from the developer》、両ファクトシートの《　》/[ ] |
| 発売時期・価格を入れる | `index.html` の製品情報の表（日英）、両ファクトシートの製品情報 |
| 開発者名義・メールを変える | 製品情報、連絡先、フッター（`© Nulpoyo`）、両ファクトシート |
| トレーラーを YouTube へ切り替える | 下の「トレーラー」。ファクトシートのトレーラー欄も |
| スクリーンショットを原寸へ差し替える | 下の「スクリーンショットの差し替え待ち」 |
| スクリーンショット・GIF を足す | 下の「素材を追加したときの手順」 |
| 説明文・キャプションの言い回し | 日英の対（`l-ja` / `l-en`）を両方直す |

**どの編集でも、最後に `python build_zip.py` で zip を作り直す。**ファクトシートと素材は zip にも入っている。
公開後なら Releases へ上げ直し、コミットして push する。

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
├── build_zip.py        一括ダウンロード用の zip を作る
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

- スクリーンショット **9枚**（**800×450 の JPEG。原寸ではない**。下記「スクリーンショットの差し替え待ち」）
- GIF **9点**（616×346）と、同じ場面のループ動画（mp4、無音）9点
  - ページ上は mp4 を再生し、GIF はダウンロード用。GIF を9本並べるとページが50MB近くになるため
  - 画面に入ったものだけ再生し、外れたら止める（`index.html` 末尾のスクリプト）
- ロゴ（透過 PNG）、キーアート（ロゴあり・なし）、Steam のカプセル・ライブラリ画像の計10点（`assets/branding/`）
- ファクトシート 日英
- トレーラー（約100秒、29MB に再圧縮した mp4）
- 一括ダウンロード用 zip（67MB。トレーラーは容量の都合で含めない）

### 未収録（決まり次第、足す）

| 何 | 備考 |
| --- | --- |
| スクリーンショットの原寸 | 下記「スクリーンショットの差し替え待ち」 |
| 開発者からのひとこと | `index.html` と `fact_sheet_*.txt` の《　》 |
| トレーラーの YouTube 版 | 下記「トレーラー」 |
| 発売時期・価格 | いまは「未定」 |

## 素材の出どころ

| ここ | ゲーム本体側の素材ID・元のファイル |
| --- | --- |
| `assets/gifs/01_meteor_start.gif` 〜 `09_awards.gif` | GIF 一式 `01_同時スタートに隕石_none_16x9_v01.gif` 〜 `09_表彰式_none_16x9_v01.gif`（番号は同じ） |
| `assets/images/01_sticky_wall.jpg` 〜 `09_beach_putt.jpg` | Steam ストアページに載せたスクリーンショットを、ストアの表示サイズ（`ss_<hash>.800x600.jpg`、実寸 800×450）で保存したもの。対応は下表 |
| `assets/gifs/loop_*.mp4` | 上の GIF を ffmpeg で mp4 にしたもの（下記） |
| `assets/branding/capsule_*`・`keyart_nologo_*` | `20261004_Steamストアカプセル` の `01_heli_hit`（`_logo_` 付きがカプセル、無しがキーアート） |
| `assets/branding/capsule_library_600x900.png`・`library_header_920x430.png`・`hero_3840x1240.png`・`logo_1280x563.png` | `20261002_Steamライブラリ` の採用版 |
| `assets/branding/app_icon.svg` | `20261002_アプリアイコン/app_icon.svg` |
| `assets/video/CrazyCityGolf_Trailer.mp4` | `20261001_steam_promo_90s` の `steam_promo_en_16x9_v20.mp4` |

| ここ | 受け取ったファイル |
| --- | --- |
| `01_sticky_wall.jpg` | `ss_653b8b33142e7dd52b57488bd6c43cda6dffa4bc.800x600.jpg` |
| `02_island_eight_players.jpg` | `ss_477cb59c4ee11a6f3001fb31d34a354a8e27d13f.800x600.jpg` |
| `03_side_gravity.jpg` | `ss_be50ce693a1a015c7492f73fb6d7b2a4fc2501bf.800x600.jpg` |
| `04_super_bounce.jpg` | `ss_db9d2150570e070ac721e492a6b14355d67875aa.800x600.jpg` |
| `05_big_ball.jpg` | `ss_020467b212578fa9e1f987241e6de8b3e88f96e1.800x600.jpg` |
| `06_amusement_park.jpg` | `ss_e978d1b53e114c333fc22ad49d9a05d6ad4560a2.800x600.jpg` |
| `07_night_harbor.jpg` | `ss_a248e2dd70d22e235b64c7694183e3567d4cd7cb.800x600.jpg` |
| `08_storm_lightning.jpg` | `ss_de797a15571aecf855c8d37cee6e82fbb7a0cf46.800x600.jpg` |
| `09_beach_putt.jpg` | `ss_83be64ced3885aaf984fd6e9b1951a0676eda431.800x600.jpg` |

### スクリーンショットの差し替え待ち

いまの9枚は、Steam が配信用に縮めた 800×450 の JPEG である。**配布物としては小さく、圧縮の滲みもある。**
編集部は記事用に切り出して拡大するので、原寸（1920×1080 の PNG。Steamworks へ上げた元ファイル）が見つかったら差し替える。

1. `assets/images/` へ同じ番号・名前の `.png` で置き、`.jpg` を消す
2. `python build_thumbs.py`
3. `index.html` のスクリーンショットの `href` と `src` を `.png` に直し、説明文の「800×450」と原寸を送る旨の文を消す
4. `python build_zip.py` で zip を作り直して Releases へ上げる

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

素材やファクトシートを直したら zip も作り直し、**Releases へ上書きアップロードする**。
zip 自体はコミットされない。容量が変わったら `index.html` のボタンの表記（日英2か所）も直す。

```bash
python build_zip.py
gh release upload assets downloads/CrazyCityGolf_PressKit.zip --clobber
```

## 素材を追加したときの手順

1. スクリーンショットは `assets/images/`（原寸）へ置く。命名は `<番号>_<名前>.png`
2. `python build_thumbs.py` を実行して縮小版を作り直す
3. `index.html` の対応する grid に `<figure>` を足す（`figcaption` は日英の対で書く）
4. `python build_zip.py` で zip を作り直し、Releases へ上書きアップロードする
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
