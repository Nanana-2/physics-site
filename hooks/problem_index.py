"""Build a compact, searchable index of all exercise pages."""

import json
import re
import unicodedata
from pathlib import Path

import yaml


SUBJECT_DIRS = (
    "01mechanics",
    "02electromagnetism",
    "03thermodynamics",
    "04quantum_mechanics",
    "05statistical_mechanics",
)


def _pages_title(directory: Path, fallback: str) -> str:
    pages_file = directory / ".pages"
    if not pages_file.exists():
        return fallback

    try:
        data = yaml.safe_load(pages_file.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return fallback
    return str(data.get("title", fallback)).strip()


def _front_matter(markdown: str) -> dict:
    if not markdown.startswith("---"):
        return {}

    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", markdown, re.DOTALL)
    if not match:
        return {}

    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _heading(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def _question_text(markdown: str) -> str:
    match = re.search(
        r"^##\s+問題\s*$\n(.*?)(?=^##\s+解説\s*$|\Z)",
        markdown,
        re.MULTILINE | re.DOTALL,
    )
    text = match.group(1) if match else ""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[[^]]*]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_>#|]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return unicodedata.normalize("NFKC", text).strip()


def _sort_key(path: Path):
    return tuple(
        (0, int(part)) if part.isdigit() else (1, part)
        for part in path.stem.split("_")
    )


def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    problems = []

    for subject_order, subject_slug in enumerate(SUBJECT_DIRS):
        subject_dir = docs_dir / subject_slug
        if not subject_dir.exists():
            continue

        subject = _pages_title(subject_dir, subject_slug)
        chapter_dirs = sorted(
            (path for path in subject_dir.iterdir() if path.is_dir()),
            key=lambda path: (
                (0, int(path.name)) if path.name.isdigit() else (1, path.name)
            ),
        )

        for chapter_dir in chapter_dirs:
            chapter = _pages_title(chapter_dir, chapter_dir.name)
            markdown_files = sorted(chapter_dir.glob("*.md"), key=_sort_key)

            for markdown_file in markdown_files:
                markdown = markdown_file.read_text(encoding="utf-8")
                metadata = _front_matter(markdown)
                tags = metadata.get("tags", [])
                if isinstance(tags, str):
                    tags = [tags]

                difficulty = next(
                    (tag for tag in ("基本", "標準", "発展") if tag in tags),
                    "未設定",
                )
                title = _heading(markdown, markdown_file.stem)
                relative_path = markdown_file.relative_to(docs_dir).with_suffix("")

                problems.append(
                    {
                        "title": title,
                        "url": relative_path.as_posix() + "/",
                        "subject": subject,
                        "subjectSlug": subject_slug,
                        "subjectOrder": subject_order,
                        "chapter": chapter,
                        "chapterSlug": chapter_dir.name,
                        "difficulty": difficulty,
                        "searchText": _question_text(markdown),
                    }
                )

    output = site_dir / "problem-index.json"
    output.write_text(
        json.dumps({"problems": problems}, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
