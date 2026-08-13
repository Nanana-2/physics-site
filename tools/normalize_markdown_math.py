#!/usr/bin/env python3
"""Markdown の表示数式区切りを MkDocs/MathJax 向けに正規化する。"""

from __future__ import annotations

import argparse
from pathlib import Path


def normalize(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    lines = source.splitlines()
    output: list[str] = []
    in_display = False
    indent = 0

    for line in lines:
        stripped = line.strip()

        # 閉じ区切りが数式の末尾へ付着した旧形式を分離する。
        if in_display and stripped.endswith("$$") and stripped != "$$":
            content = line[: line.rfind("$$")].rstrip()
            if indent and content.startswith(" " * indent):
                content = content[indent:]
            output.append(content)
            output.append("$$")
            output.append("")
            in_display = False
            indent = 0
            continue

        if stripped == "$$":
            if not in_display:
                if output and output[-1] != "":
                    output.append("")
                indent = len(line) - len(line.lstrip())
                output.append("$$")
                in_display = True
            else:
                output.append("$$")
                output.append("")
                in_display = False
                indent = 0
            continue

        if in_display and indent and line.startswith(" " * indent):
            line = line[indent:]
        output.append(line.rstrip())

    # 連続する空行は1行へまとめる。
    compact: list[str] = []
    for line in output:
        if line == "" and compact and compact[-1] == "":
            continue
        compact.append(line)
    while compact and compact[-1] == "":
        compact.pop()
    normalized = "\n".join(compact) + "\n"
    if normalized == source:
        return False
    path.write_text(normalized, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    changed = 0
    for root in args.paths:
        files = [root] if root.is_file() else sorted(root.rglob("*.md"))
        for path in files:
            changed += normalize(path)
    print(f"normalized {changed} files")


if __name__ == "__main__":
    main()
