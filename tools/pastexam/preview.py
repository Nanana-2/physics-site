"""過去問のドラフトを，手元のサイトで確認できるようにする。

    python3 tools/pastexam/preview.py          # 写すだけ
    python3 tools/pastexam/preview.py --serve  # 写して mkdocs serve を立ち上げる（http://127.0.0.1:8001/_pastexam_preview/）

pastexam/<大学>/drafts/*.md を docs/_pastexam_preview/<大学>/ に写し，図のパスを写した先に合わせて直す。
docs/_pastexam_preview/ は .gitignore に入っているので，コミットも公開もされない。ドラフトを直したら，もう一度実行する。
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "pastexam"
DST = ROOT / "docs" / "_pastexam_preview"


def main():
    if DST.exists():
        shutil.rmtree(DST)
    links = []
    for drafts in sorted(SRC.glob("*/drafts")):
        univ = drafts.parent.name
        out = DST / univ
        out.mkdir(parents=True)
        for md in sorted(drafts.glob("*.md")):
            text = md.read_text(encoding="utf-8").replace("../../../docs/assets/", "../../assets/")
            (out / md.name).write_text(text, encoding="utf-8")
            title = re.search(r"^title:\s*(.+)$", text, re.M)
            links.append(f"- [{title.group(1) if title else md.stem}]({univ}/{md.name})")
    (DST / "index.md").write_text("# 過去問の確認用（公開しない）\n\n" + "\n".join(links) + "\n", encoding="utf-8")
    print(f"{len(links)} 問を docs/_pastexam_preview/ に写しました。")
    if "--serve" in sys.argv:
        print("http://127.0.0.1:8001/_pastexam_preview/")
        subprocess.run([sys.executable, "-m", "mkdocs", "serve", "-a", "127.0.0.1:8001"], cwd=ROOT)


if __name__ == "__main__":
    main()
