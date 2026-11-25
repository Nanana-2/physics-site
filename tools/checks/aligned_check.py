"""aligned の中で，& のない行がほかの行と混ざっているところを探す。

& のない行は左の列に右寄せで置かれるので，ほかの行と位置がずれる。
使い方：python3 tools/checks/aligned_check.py <ファイルかフォルダ> ...
"""
import pathlib
import re
import sys

NESTED = r"\\begin\{(pmatrix|bmatrix|vmatrix|Vmatrix|matrix|smallmatrix|cases|array)\}.*?\\end\{\1\}"


def rows(body):
    body = re.sub(NESTED, "M", body, flags=re.S)
    body = re.sub(r"\\substack\{(?:[^{}]|\{[^{}]*\})*\}", "S", body)
    return [r for r in re.split(r"\\\\", body) if r.strip()]


def check(path):
    text = path.read_text(encoding="utf-8")
    found = 0
    for m in re.finditer(r"\\begin\{aligned\}(.*?)\\end\{aligned\}", text, flags=re.S):
        counts = [r.count("&") for r in rows(m.group(1))]
        if len(counts) >= 2 and 0 in counts and any(counts):
            line = text[: m.start()].count("\n") + 1
            print(f"{path}:{line}: & のない行があります（行ごとの & の数 {counts}）")
            found += 1
    return found


def main():
    paths = []
    for arg in sys.argv[1:] or ["docs", "pastexam"]:
        p = pathlib.Path(arg)
        paths += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    total = sum(check(p) for p in paths if "_pastexam_preview" not in p.parts)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
