"""別の AI の出力（outputs/batch_XX.md）を1問1ファイルに分け，形式を点検し，図の依頼を一覧にする（Claude 用）。

    python3 import_outputs.py outputs/batch_01.md [...]

- generated/<分野>/<章>/<ファイル> に書き出す（docs/ にはまだ入れない）
- 形式の問題（見出し・区切り・tags・問題文中の \finalanswer・$ の内側の空白）を表示
- 図の依頼を generated/FIGURES.md に追記する
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "generated"
SEP = re.compile(r"^===== FILE: (\S+) =====\s*$", re.M)


def check(path: str, text: str) -> list:
    issues = []
    if not re.match(r"---\ntags:\n  - (基本|標準|発展)\n---\n", text):
        issues.append("front matter / tags")
    for head in ("\n## 問題\n", "\n---\n\n## 解答・解説\n"):
        if head not in text:
            issues.append(f"missing {head.strip()!r}")
    problem = text.split("## 解答・解説")[0]
    if "\\finalanswer" in problem.split("## 問題", 1)[-1]:
        issues.append("\\finalanswer in problem statement")
    if "\\finalanswer" not in text:
        issues.append("no \\finalanswer")
    inline = re.findall(r"(?<!\$)\$([^$\n]+)\$", re.sub(r"\$\$.*?\$\$", "", text, flags=re.S))
    if any(m != m.strip() for m in inline):
        issues.append("space inside $...$")
    if "\\\\\\\\" in text:
        issues.append("\\\\\\\\ line break")
    if re.search(r"\$\$\s*\n[^$]*\n\$\$\s*\n\s*\n### |\$\$\s*$", text.strip()):
        issues.append("ends on a bare equation (no closing sentence)")
    return issues


def main():
    figures = []
    for src in sys.argv[1:]:
        raw = Path(src).read_text(encoding="utf-8").replace("===== END =====", "")
        parts = SEP.split(raw)
        print(f"== {src}: {len(parts) // 2} files")
        for i in range(1, len(parts), 2):
            rel, body = parts[i], parts[i + 1].strip() + "\n"
            dest = OUT / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(body, encoding="utf-8")
            issues = check(rel, body)
            if issues:
                print(f"  {rel}: {', '.join(issues)}")
            for m in re.finditer(r"<!-- FIGURE (problem|solution[^:]*): (.*?) -->", body, re.S):
                figures.append(f"- `{rel}` [{m.group(1)}] {m.group(2).strip()}")
    if figures:
        with (OUT / "FIGURES.md").open("a", encoding="utf-8") as f:
            f.write("\n".join(figures) + "\n")
        print(f"{len(figures)} figure requests -> generated/FIGURES.md")


if __name__ == "__main__":
    main()
