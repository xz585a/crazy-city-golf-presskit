"""一括ダウンロード用の zip を downloads/ に作り直す。

素材やファクトシートを直したら実行し、Releases へ上書きアップロードする。
zip 自体は Git に入れない（.gitignore）。

    python build_zip.py
    gh release upload assets downloads/CrazyCityGolf_PressKit.zip --clobber

容量が変わったら、index.html のダウンロードボタンの「(NN MB)」も直す。
トレーラーは容量の都合で含めない。
"""

import os
import zipfile

OUT = "downloads/CrazyCityGolf_PressKit.zip"
ROOT = "CrazyCityGolf_PressKit/"
TEXTS = ["fact_sheet_ja.txt", "fact_sheet_en.txt"]
DIRS = ["assets/images", "assets/gifs", "assets/branding"]


def main() -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if os.path.exists(OUT):
        os.remove(OUT)

    count = 0
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for f in TEXTS:
            z.write(f, ROOT + f)
            count += 1
        for sub in DIRS:
            for f in sorted(os.listdir(sub)):
                if f.startswith("."):
                    continue
                z.write(os.path.join(sub, f), ROOT + os.path.basename(sub) + "/" + f)
                count += 1

    size_mb = os.path.getsize(OUT) / 1024 / 1024
    print("%s: %d files, %.0f MB" % (OUT, count, size_mb))


if __name__ == "__main__":
    main()
