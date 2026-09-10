"""Generate concise, unique metadata for exercise pages.

The Markdown files remain the source of truth.  Descriptions are derived at
build time so that hundreds of exercise pages do not need duplicated YAML
front matter.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml


SUBJECT_NAMES = {
    "01mechanics": "力学",
    "02electromagnetism": "電磁気学",
    "03thermodynamics": "熱力学",
    "04quantum_mechanics": "量子力学",
    "05statistical_mechanics": "統計力学",
}

PAGE_DESCRIPTIONS = {
    "index.md": "力学・電磁気学・熱力学・量子力学・統計力学の演習問題と解答・解説を掲載する、大学物理の問題集です。",
    "tags.md": "大学物理の演習問題を、分野・章・難易度・キーワードから絞り込んで探せます。",
    "tag-index.md": "大学物理の問題集で使用している基本・標準・発展の難易度タグを確認できます。",
    "books.md": "大学物理の学習と演習問題の作成で参考にした教科書・参考書を、分野別に紹介します。",
    "privacy.md": "大学物理の問題集におけるアクセス解析、広告・アフィリエイト、Cookieなどの取り扱いを説明します。",
    "terms.md": "大学物理の問題集の利用条件、著作権、免責事項、生成AIの利用方針について説明します。",
}


def _pages_title(directory: Path, fallback: str) -> str:
    pages_file = directory / ".pages"
    if not pages_file.exists():
        return fallback
    try:
        data = yaml.safe_load(pages_file.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return fallback
    title = str(data.get("title", fallback)).strip()
    return re.sub(r"^\d+[.．]\s*", "", title)


def _heading(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def on_page_markdown(markdown, page, config, files, **kwargs):
    """Attach a description to problem pages that do not define one."""
    if "description" in page.meta:
        return markdown

    source = Path(page.file.src_uri)
    parts = source.parts

    if source.as_posix() in PAGE_DESCRIPTIONS:
        page.meta["description"] = PAGE_DESCRIPTIONS[source.as_posix()]
        return markdown

    if len(parts) == 2 and parts[0] in SUBJECT_NAMES and parts[1] == "index.md":
        subject = SUBJECT_NAMES[parts[0]]
        page.meta["description"] = (
            f"{subject}の演習問題を章別に掲載しています。"
            "各問題には解答・解説があり、大学の定期試験や大学院入試の学習に利用できます。"
        )
        return markdown

    if len(parts) != 3 or parts[0] not in SUBJECT_NAMES or not parts[1].isdigit():
        return markdown

    title = _heading(markdown, page.title or source.stem)
    chapter_dir = Path(config["docs_dir"]) / parts[0] / parts[1]
    chapter = _pages_title(chapter_dir, f"第{int(parts[1])}章")
    subject = SUBJECT_NAMES[parts[0]]

    page.meta["description"] = (
        f"{subject}の「{title}」に関する演習問題です。"
        f"{chapter}の問題文と解答・解説を掲載しています。"
    )
    return markdown
