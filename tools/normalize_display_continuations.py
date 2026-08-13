#!/usr/bin/env python3
"""表示数式が等号だけで始まる箇所へ、直前の数式の左辺を補う。"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


EQUAL = re.compile(r"(?<![<>!])=(?!=)")


def formula_lines(body: list[str]) -> list[str]:
    return [line.strip() for line in body if line.strip() and not line.strip().startswith((r"\begin{", r"\end{"))]


def lhs_of(body: list[str]) -> str | None:
    for line in formula_lines(body):
        candidate = line
        if candidate.startswith(r"\finalanswer{"):
            candidate = candidate[len(r"\finalanswer{") :]
        if "&=" in candidate:
            lhs = candidate.split("&=", 1)[0].strip()
            if lhs:
                return lhs
            continue
        match = EQUAL.search(candidate)
        if match and match.start() > 0:
            return candidate[: match.start()].strip()
    return None


def normalize(path: Path, write: bool) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[tuple[int, int]] = []
    opening: int | None = None
    for index, line in enumerate(lines):
        if line == "$$":
            if opening is None:
                opening = index
            else:
                blocks.append((opening, index))
                opening = None

    changed = 0
    for block_index in range(1, len(blocks)):
        start, end = blocks[block_index]
        body = lines[start + 1 : end]
        if any(r"\begin{aligned}" in line for line in body):
            continue
        first_index = next((i for i, line in enumerate(body) if line.strip()), None)
        if first_index is None or not body[first_index].strip().startswith("="):
            continue
        previous_start, previous_end = blocks[block_index - 1]
        between = lines[previous_end + 1 : start]
        if any(line.startswith(("#", "---")) for line in between):
            continue
        lhs = lhs_of(lines[previous_start + 1 : previous_end])
        if not lhs:
            continue
        old = body[first_index].strip()
        print(f"{path}:{start + 2}: {lhs} {old[:72]}")
        if write:
            indent = body[first_index][:-len(body[first_index].lstrip())]
            lines[start + 1 + first_index] = f"{indent}{lhs} {old}"
        changed += 1

    if write and changed:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    total = 0
    for root in args.paths:
        files = [root] if root.is_file() else sorted(root.rglob("*.md"))
        total += sum(normalize(path, args.write) for path in files)
    print(f"{'normalized' if args.write else 'found'} {total} continuations")


if __name__ == "__main__":
    main()
