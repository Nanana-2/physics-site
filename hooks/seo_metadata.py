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
    "06solid_state": "物性物理学",
    "14calculus": "微積分",
    "07linear_algebra": "線形代数",
    "08differential_equations": "微分方程式",
    "09vector_analysis": "ベクトル解析",
    "10integral_transforms": "積分変換",
    "11complex_analysis": "複素関数",
    "12special_functions": "特殊関数・変分法",
    "13probability_statistics": "確率・統計",
}

PAGE_DESCRIPTIONS = {
    "index.md": "力学・電磁気学・熱力学・量子力学・統計力学・物性物理学と物理数学の演習問題と解答・解説を掲載する、大学物理の問題集です。",
    "tags.md": "大学物理の演習問題を、分野・章・難易度・キーワードから絞り込んで探せます。",
    "exam.md": "好きな問題を8問まで選んで、問題用紙と解答・解説を印刷できます。",
    "tag-index.md": "大学物理の問題集で使用している基本・標準・発展の難易度タグを確認できます。",
    "books.md": "大学物理の学習と演習問題の作成で参考にした教科書・参考書を、分野別に紹介します。",
    "privacy.md": "大学物理の問題集におけるアクセス解析、広告・アフィリエイト、Cookieなどの取り扱いを説明します。",
    "pastexam/index.md": "大学院入試（院試）の物理学・数学の過去問に、独自の解答・解説を付けて掲載しています。",
    "pastexam/todai-ributsu/index.md": "東京大学大学院理学系研究科物理学専攻（東大理物）の院試過去問を年度別に掲載し、独自の解答・解説を付けています。",
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


def _western_year(era_year: str) -> str:
    """「令和8年度」→「2026年度」。和暦でなければ空文字を返す。"""
    match = re.match(r"(令和|平成)(\d+|元)年度", era_year)
    if not match:
        return ""
    number = 1 if match.group(2) == "元" else int(match.group(2))
    base = 2018 if match.group(1) == "令和" else 1988
    return f"{base + number}年度"


def _exam_description(meta) -> str:
    title = str(meta.get("title", ""))
    topic = title.split("：", 1)[1].strip() if "：" in title else ""
    year = str(meta.get("exam_year", ""))
    western = _western_year(year)
    year_text = f"{year}（{western}）" if western else year
    subject = str(meta.get("exam_subject", ""))
    number = str(meta.get("exam_number", ""))
    university = str(meta.get("exam_university", ""))
    head = f"{university}の{year_text}院試、{subject} {number}"
    if topic:
        head += f"「{topic}」"
    return head + "の問題と独自の解答・解説です。"


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

    if page.meta.get("exam_number") and page.meta.get("exam_university"):
        page.meta["description"] = _exam_description(page.meta)
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
