#!/usr/bin/env python3
"""サイトの問題MarkdownをPDF版のLaTeX断片へ変換する。"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def escape_text(text: str) -> str:
    """インライン数式を保ったまま，LaTeXの予約文字を処理する。"""
    parts = re.split(r"(\$[^$]+\$)", text)
    escaped: list[str] = []
    for part in parts:
        if part.startswith("$") and part.endswith("$"):
            escaped.append(part)
            continue
        part = part.replace("&", r"\&")
        part = part.replace("%", r"\%")
        part = part.replace("#", r"\#")
        part = part.replace("_", r"\_")
        escaped.append(part)
    return "".join(escaped)


def convert_blocks(lines: list[str]) -> list[str]:
    """Markdown本文をLaTeX本文へ変換する。"""
    result: list[str] = []
    paragraph: list[str] = []
    in_display = False
    display: list[str] = []

    def flush_paragraph() -> bool:
        if paragraph:
            result.append(escape_text(" ".join(part.strip() for part in paragraph)))
            paragraph.clear()
            return True
        return False

    for raw in lines:
        line = raw.rstrip()
        if line.strip() == "$$":
            if in_display:
                result.append(r"\begin{equation*}")
                result.extend(display)
                result.append(r"\end{equation*}")
                display.clear()
                in_display = False
            else:
                flush_paragraph()
                if result and result[-1] == r"\par":
                    result.pop()
                in_display = True
            continue
        if in_display:
            # Markdown側では改行命令が二重にエスケープされている場合がある。
            display.append(line.replace("\\\\\\\\", "\\\\"))
            continue
        if not line.strip() or line.strip() == "---":
            if flush_paragraph():
                result.append(r"\par")
            continue
        paragraph.append(line)

    flush_paragraph()
    if result and result[-1] == r"\par":
        result.pop()
    return result


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError("YAML front matter が見つかりません")
    return match.group(1), match.group(2)


def extract_tag(frontmatter: str) -> str:
    match = re.search(r"(?m)^\s*-\s*(.+?)\s*$", frontmatter)
    if not match:
        raise ValueError("難易度タグが見つかりません")
    return match.group(1)


def numbered_parts(lines: list[str]) -> tuple[list[str], list[tuple[str, list[str]]]]:
    intro: list[str] = []
    parts: list[tuple[str, list[str]]] = []
    current_number: str | None = None
    current_lines: list[str] = []

    for line in lines:
        match = re.match(r"^\((\d+)\)\s*(.*)$", line)
        if match:
            if current_number is not None:
                parts.append((current_number, current_lines))
            current_number = match.group(1)
            current_lines = [match.group(2)]
        elif current_number is None:
            intro.append(line)
        else:
            current_lines.append(line)

    if current_number is not None:
        parts.append((current_number, current_lines))
    return intro, parts


def convert_file(source: Path, destination: Path) -> None:
    frontmatter, body = split_frontmatter(source.read_text(encoding="utf-8"))
    tag = extract_tag(frontmatter)

    title_match = re.search(r"(?m)^# (.+)$", body)
    problem_match = re.search(r"(?ms)^## 問題\n(.*?)\n---\n\n## 解説\n", body)
    solution_match = re.search(r"(?ms)^## 解説\n(.*)\Z", body)
    if not (title_match and problem_match and solution_match):
        raise ValueError(f"見出し構造を解釈できません: {source}")

    title = title_match.group(1).strip()
    problem_lines = problem_match.group(1).splitlines()
    solution_text = solution_match.group(1)
    intro, questions = numbered_parts(problem_lines)

    stem = source.stem
    chapter, item = stem.split("_")
    problem_number = f"{int(chapter)}.{int(item) // 10}"

    output: list[str] = [
        rf"\problemstart",
        rf"\addcontentsline{{toc}}{{section}}{{{problem_number}　{escape_text(title)}}}",
        "",
        (
            rf"\begin{{problemBox}}{{問題 {problem_number}\quad "
            rf"{escape_text(title)}\hspace{{1.2em}}{{\small\mdseries 〔{escape_text(tag)}〕}}}}"
        ),
    ]
    output.extend(convert_blocks(intro))
    output.extend(["", r"\begin{enumerate}"])
    for _number, question_lines in questions:
        converted = convert_blocks(question_lines)
        if not converted:
            continue
        output.append(r"  \item " + converted[0])
        output.extend("  " + line for line in converted[1:])
        output.append("")
    if output[-1] == "":
        output.pop()
    output.extend([r"\end{enumerate}", r"\end{problemBox}", "", r"\solutionheading"])
    output.append(r"\begin{solutionparts}")

    solution_sections = re.split(r"(?m)^### \((\d+)\)\s*$", solution_text)
    for index in range(1, len(solution_sections), 2):
        number = solution_sections[index]
        section_lines = solution_sections[index + 1].strip().splitlines()
        output.extend(["", rf"\solutionpart{{({number})}}"])
        output.extend(convert_blocks(section_lines))

    output.extend(["", r"\end{solutionparts}", ""])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(output), encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: convert_problem.py SOURCE.md DESTINATION.tex")
    convert_file(Path(sys.argv[1]), Path(sys.argv[2]))


if __name__ == "__main__":
    main()
