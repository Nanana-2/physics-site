"""`<div markdown>` などの中で，数式の `<` のすぐ後に英字が続くところを探す。

    python3 tools/checks/lt_check.py            # docs と pastexam の下をすべて
    python3 tools/checks/lt_check.py docs/06solid_state

考え方（`<div class="approach" markdown>`）や補足（`<aside ... markdown>`）の中では，
`$0<x<L$` の `<x` が HTML のタグの始まりと読まれ，閉じタグがずれてページの組み方が崩れる。
`$0 < x < L$` のように `<` の前後に空白を入れる。見つかれば一覧を出して 1 で終わる。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOCK = re.compile(r"<(div|aside|figure)[^>]*markdown[^>]*>(.*?)</\1>", re.S)
MATH = re.compile(r"\$[^$]*\$")


def main():
    targets = [Path(a) for a in sys.argv[1:]] or [ROOT / "docs", ROOT / "pastexam"]
    found = 0
    for target in targets:
        for md in sorted(target.rglob("*.md") if target.is_dir() else [target]):
            if "_pastexam_preview" in md.parts:
                continue
            text = md.read_text(encoding="utf-8")
            for block in BLOCK.finditer(text):
                for math in MATH.finditer(block.group(2)):
                    if re.search(r"<[A-Za-z]", math.group(0)):
                        line = text.count("\n", 0, block.start(2) + math.start()) + 1
                        print(f"{md.relative_to(ROOT)}:{line}: {math.group(0)}")
                        found += 1
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
