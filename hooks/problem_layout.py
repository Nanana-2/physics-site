"""問題ページの組版：問題文を枠で囲み，難易度の★と小問のぶら下げインデントを付ける。

Markdown 側は今まで通り「## 問題」…「---」…「## 解答・解説」と書けばよく，
ここで HTML を次の形に組み替える（見出しの id はそのまま残すので目次はそのまま使える）。

    <div class="problem-box">
      <h2 id="..."><span>問題</span><span class="problem-stars">★☆☆</span></h2>
      <div class="problem-box__body"> 問題文（小問は p.subq） </div>
    </div>

タイトルの h1 には class="problem-title" を付け，パンくずはタイトルの下へ移す。
分野別の問題一覧（<分野>/index.md）は，章ごとのカードを番号・タイトル・★の目次に組み替える。
"""

import re
from pathlib import Path

import yaml

SUBJECT_DIRS = (
    "01mechanics",
    "02electromagnetism",
    "03thermodynamics",
    "04quantum_mechanics",
    "05statistical_mechanics",
)
LEVELS = {"基本": 1, "標準": 2, "発展": 3}

PROBLEM_HEADING = re.compile(r'<h2 id="([^"]+)">問題</h2>')
SUBQUESTION = re.compile(r"<p>\((\d+)\)\s*(.*?)</p>", re.DOTALL)


def _level_from_tags(tags) -> int:
    if isinstance(tags, str):
        tags = [tags]
    return next((LEVELS[tag] for tag in tags or [] if tag in LEVELS), 0)


def _stars_html(level: int, cls: str) -> str:
    if not level:
        return ""
    return (
        f'<span class="{cls}" aria-label="難易度 {level}/3">'
        f'<span class="on">{"★" * level}</span><span class="off">{"☆" * (3 - level)}</span></span>'
    )


def _stars(meta) -> str:
    level = _level_from_tags(meta.get("tags"))
    if not level:
        return ""
    return (
        f'<span class="problem-stars" aria-label="難易度 {level}/3">'
        f'<span class="problem-stars__on">{"★" * level}</span>'
        f'<span class="problem-stars__off">{"☆" * (3 - level)}</span></span>'
    )


def _indent_continuations(body: str) -> str:
    """小問の途中に別行立ての数式や箇条書きがあるとき，その後ろ（次の小問まで）も小問の本文と同じだけ下げる。"""
    parts = body.split('<p class="subq">')
    for i in range(1, len(parts)):
        end = parts[i].index("</p>") + len("</p>")
        rest = parts[i][end:]
        if rest.strip():
            parts[i] = parts[i][:end] + f'<div class="subq__cont">{rest}</div>'
    return '<p class="subq">'.join(parts)


def on_page_content(html, page, config, files):
    if not page.file.src_uri.startswith(SUBJECT_DIRS):
        return html
    if page.file.src_uri.endswith("/index.md"):
        return _subject_index(html, page, config)
    heading = PROBLEM_HEADING.search(html)
    if not heading:
        return html
    # 問題文は「問題」の見出しから，解答の前の区切り線（---）まで
    rule = re.compile(r"<hr\s*/?>").search(html, heading.end())
    if not rule:
        return html

    body = html[heading.end() : rule.start()]
    body = SUBQUESTION.sub(
        lambda m: f'<p class="subq"><span class="subq__number">({m.group(1)})</span>'
        f"<span>{m.group(2)}</span></p>",
        body,
    )
    body = _indent_continuations(body)
    box = (
        '<div class="problem-box">'
        f'<h2 id="{heading.group(1)}"><span>問題</span>{_stars(page.meta)}</h2>'
        f'<div class="problem-box__body">{body}</div>'
        "</div>"
    )
    rest = html[rule.end() :]
    # 解答・解説の帯と，小問ごとの小見出し（(1) の右に細い線）
    rest = re.sub(r'<h2 id="([^"]+)">解答・解説</h2>', r'<h2 id="\1" class="solution-heading">解答・解説</h2>', rest, count=1)
    rest = re.sub(r'<h3 id="([^"]+)">', r'<h3 id="\1" class="solution-part">', rest)
    head = re.sub(r"<h1 ", '<h1 class="problem-title" ', html[: heading.start()], count=1)
    return head + box + rest


BREADCRUMB = re.compile(r'<nav class="md-path".*?</nav>\s*', re.DOTALL)
ARTICLE_START = '<article class="md-content__inner md-typeset">'


def on_post_page(output, page, config):
    # パンくずは本文の中へ移して左端をそろえる。タイトルがあればその（下線の）下，なければ本文の先頭
    nav = BREADCRUMB.search(output)
    article = output.find(ARTICLE_START, nav.end()) if nav else -1
    if article < 0:
        return output
    title_end = output.find("</h1>", article)
    at = title_end + len("</h1>") if title_end >= 0 else article + len(ARTICLE_START)
    return output[: nav.start()] + output[nav.end() : at] + nav.group(0) + output[at:]


# ---- 分野別の問題一覧：章ごとのカードを目次（番号・タイトル・★）に組み替える ----

CHAPTER_CARD = re.compile(
    r"<li>\s*<p><strong>(\d+)\.\s*(.*?)</strong></p>\s*<hr\s*/?>\s*<ul>(.*?)</ul>\s*</li>", re.DOTALL
)
CARD_GRID = re.compile(r'<div class="grid cards">.*?</div>', re.DOTALL)


def _level(md_path: Path) -> int:
    try:
        text = md_path.read_text(encoding="utf-8")
        meta = yaml.safe_load(re.match(r"---\s*\n(.*?)\n---", text, re.DOTALL).group(1)) or {}
    except (OSError, AttributeError, yaml.YAMLError):
        return 0
    return _level_from_tags(meta.get("tags"))


def _subject_index(html, page, config):
    base = Path(config["docs_dir"]) / Path(page.file.src_uri).parent
    grid = CARD_GRID.search(html)
    if not grid:
        return html
    sections = []
    for number, title, items in CHAPTER_CARD.findall(grid.group(0)):
        links = re.findall(r'<a href="([^"]+)">(.*?)</a>', items)
        rows = "".join(
            f'<a class="toc-row" href="{href}"><span class="toc-row__num">{number}-{i}</span>'
            f'<span class="toc-row__title">{name}</span>{_stars_html(_level(base / (href.strip("/") + ".md")), "toc-row__stars")}</a>'
            for i, (href, name) in enumerate(links, 1)
        )
        sections.append(
            f'<section class="toc-chapter"><h2 class="toc-chapter__head"><span class="toc-chapter__no">{number}</span>'
            f'<span class="toc-chapter__title">{title}</span></h2>'
            f"{rows}</section>"
        )
    if not sections:
        return html
    return html[: grid.start()] + '<div class="toc">' + "".join(sections) + "</div>" + html[grid.end() :]
