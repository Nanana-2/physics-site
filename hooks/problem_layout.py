"""問題ページの組版：問題文を枠で囲み，難易度の★と小問のぶら下げインデントを付ける。

Markdown 側は今まで通り「## 問題」…「---」…「## 解答・解説」と書けばよく，
ここで HTML を次の形に組み替える（見出しの id はそのまま残すので目次はそのまま使える）。

    <div class="problem-box">
      <h2 id="..."><span>問題</span><span class="problem-stars">★☆☆</span></h2>
      <div class="problem-box__body"> 問題文（小問は p.subq） </div>
    </div>

タイトルの h1 には class="problem-title" を付け，パンくずはタイトルの下へ移す。
"""

import re

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


def _stars(meta) -> str:
    tags = meta.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    level = next((LEVELS[tag] for tag in tags if tag in LEVELS), 0)
    if not level:
        return ""
    return (
        f'<span class="problem-stars" aria-label="難易度 {level}/3">'
        f'<span class="problem-stars__on">{"★" * level}</span>'
        f'<span class="problem-stars__off">{"☆" * (3 - level)}</span></span>'
    )


def on_page_content(html, page, config, files):
    if not page.file.src_uri.startswith(SUBJECT_DIRS):
        return html
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


def on_post_page(output, page, config):
    # 問題ページのパンくずは，タイトル（とその下線）の下へ移す
    if 'class="problem-title"' not in output:
        return output
    nav = BREADCRUMB.search(output)
    title_end = output.find("</h1>", nav.end()) if nav else -1
    if title_end < 0:
        return output
    title_end += len("</h1>")
    return output[: nav.start()] + output[nav.end() : title_end] + nav.group(0) + output[title_end:]
