"""過去問の原稿をサイトのページにする。

    python3 tools/pastexam/publish.py H22 H23 R8   # 指定した年度だけ
    python3 tools/pastexam/publish.py --all        # 原稿のある年度すべて

pastexam/<大学>/drafts/<年度>_*.md を docs/pastexam/<大学>/ に写し，図のパスを写した先に合わせて直す。
続けて docs/pastexam/<大学>/.pages（年度ごとの節。新しい年度から）を，docs/pastexam/<大学>/ にあるページから作り直す。
大学のページ（年度の一覧）と院試過去問の最初のページは，ないときだけ tools/pastexam/pages/ から写す。
年度の一覧の中身は hooks/problem_layout.py がページのフロントマターから組み立てる。

上のメニューに出すには，docs/.pages の nav の books.md の前に `- pastexam` を足す（初めて公開するときの1回だけ）。
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UNIV = "todai-ributsu"
DRAFTS = ROOT / "pastexam" / UNIV / "drafts"
TEMPLATES = Path(__file__).with_name("pages")
DOCS = ROOT / "docs" / "pastexam"
OUT = DOCS / UNIV

ERA = {"R": "令和", "H": "平成"}


def year_of(stem: str) -> str:
    return stem.split("_")[0]


def year_key(year: str):
    # 令和を平成より前に，同じ元号では新しい年度から
    return (0 if year[0] == "R" else 1, -int(year[1:]))


def problem_key(stem: str):
    # 平成の年度は物理学，数学の順。番号は小さい順
    parts = stem.split("_")
    return (parts[1] if len(parts) == 3 else "", int(parts[-1]))


def write_pages():
    stems = sorted((p.stem for p in OUT.glob("*.md") if p.stem != "index"), key=problem_key)
    years = sorted({year_of(s) for s in stems}, key=year_key)
    lines = ["title: 東大理物", "nav:", "  - index.md"]
    for year in years:
        lines.append(f"  - {ERA[year[0]]}{year[1:]}年度:")
        lines += [f"    - {s}.md" for s in stems if year_of(s) == year]
    (OUT / ".pages").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(stems), len(years)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    drafts = sorted(DRAFTS.glob("*.md"))
    if "--all" not in args:
        drafts = [d for d in drafts if year_of(d.stem) in args]
    OUT.mkdir(parents=True, exist_ok=True)
    for src in TEMPLATES.rglob("*"):
        dst = DOCS / src.relative_to(TEMPLATES)
        if src.is_file() and not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(src, dst)
    for md in drafts:
        text = md.read_text(encoding="utf-8").replace("../../../docs/assets/", "../../assets/")
        (OUT / md.name).write_text(text, encoding="utf-8")
    pages, years = write_pages()
    print(f"{len(drafts)} 問を写しました。docs/pastexam/{UNIV}/ は {years} 年度，{pages} 問です。")


if __name__ == "__main__":
    main()
