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

import posixpath
import re
from pathlib import Path

import material
import yaml

SUBJECT_DIRS = (
    "01mechanics",
    "02electromagnetism",
    "03thermodynamics",
    "04quantum_mechanics",
    "05statistical_mechanics",
    "06solid_state",
    "07linear_algebra",
    "08differential_equations",
    "09vector_analysis",
    "10integral_transforms",
    "11complex_analysis",
    "12special_functions",
    "13probability_statistics",
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
    if page.file.src_uri == "books.md":
        return _books(html)
    if page.is_homepage:
        return _home(html, page, config)
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
    rest = _fold_answers(rest)
    head = re.sub(r"<h1 ", '<h1 class="problem-title" ', html[: heading.start()], count=1)
    return head + _copy_source(page) + box + rest


ANSWER_TOGGLE = '<button type="button" class="answer-toggle" data-answer-toggle hidden>解答を見る</button>'


def _fold_answers(rest: str) -> str:
    """小問ごとの解答（(1) の見出しの下から次の見出しまで）を折りたためるように包む。
    JavaScript が動かないときは全部見えたまま（javascripts/answers.js がボタンを出して閉じる）。"""
    heading = re.search(r'<h2 id="[^"]+" class="solution-heading">.*?</h2>', rest)
    if not heading:
        return rest
    before, after = rest[: heading.end()], rest[heading.end() :]
    # 末尾の補足は，最後の解答の外へ出して，押すと開く1行（details）にする
    note = ""
    m = re.search(r'<aside class="rigor-note">(.*?)</aside>\s*$', after, re.DOTALL)
    if m:
        after = after[: m.start()]
        note = ('<details class="rigor-note"><summary>'
                f'<span class="rigor-note__icon" aria-hidden="true">{_icon("circle-info")}</span>補足</summary>'
                f'<div class="rigor-note__body">{m.group(1).strip()}</div></details>')
    parts = re.split(r'(<h3 id="[^"]+" class="solution-part">.*?</h3>)', after)
    if len(parts) == 1:
        return before + ANSWER_TOGGLE + f'<div class="answer"><div class="answer__inner">{after}</div></div>' + note
    out = parts[0]
    for i in range(1, len(parts), 2):
        out += parts[i] + ANSWER_TOGGLE + f'<div class="answer"><div class="answer__inner">{parts[i + 1]}</div></div>'
    return before + out + note


def _copy_source(page) -> str:
    """「Markdown でコピー」用に，問題と解答の Markdown をページに埋め込む（図は「（図）」に置き換える）。"""
    title = page.title or ""
    text = re.sub(r"<figure.*?</figure>", "（図は省略）", page.markdown or "", flags=re.DOTALL)
    text = re.sub(r'<aside class="rigor-note" markdown>\s*(.*?)\s*</aside>', r"補足：\1", text, flags=re.DOTALL)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    text = f"# {title}\n\n{text}" if not text.startswith("# ") else text
    text = text.replace("</", "<\\/")
    return (
        '<div class="page-tools"><button type="button" class="page-tools__copy" data-copy-markdown hidden>'
        '<span class="page-tools__icon" aria-hidden="true"></span><span data-copy-label>Markdownでコピー</span></button></div>'
        f'<script type="text/markdown" id="page-markdown">{text}</script>'
    )


BREADCRUMB = re.compile(r'<nav class="md-path".*?</nav>\s*', re.DOTALL)
ARTICLE_START = '<article class="md-content__inner md-typeset">'


# パンくずの分野（と物理数学）の前にアイコンを付ける
PATH_NAME = re.compile(r'(<a [^>]*class="md-path__link"[^>]*>\s*)(<span class="md-ellipsis">\s*([^<]*?)\s*</span>)')


def _crumb_icon(m):
    icons = {name: icon for _, name, icon, _ in (*HOME_SUBJECTS, *MATH_SUBJECTS)}
    icons["物理数学"] = "square-root-variable"
    icon = icons.get(m.group(3))
    if not icon:
        return m.group(0)
    return f'{m.group(1)}<span class="md-path__icon" aria-hidden="true">{_icon(icon)}</span>{m.group(2)}'


# ---- 関連する問題：hooks/related_problems.txt のグループから，解説の下（前後の問題の上）に並べる ----
RELATED_FILE = Path(__file__).with_name("related_problems.txt")
_related_cache = {}


def _related_index(docs: Path) -> dict:
    if "index" in _related_cache:
        return _related_cache["index"]
    index = {}
    for raw in RELATED_FILE.read_text(encoding="utf-8").splitlines():
        group = raw.split("#")[0].split()
        for key in group:
            index.setdefault(key, [])
            for other in group:
                if other != key and other not in index[key]:
                    index[key].append(other)
    _related_cache["index"] = index
    return index


def _problem_info(docs: Path, key: str):
    subject, stem = key.split("/")
    chapter = stem[:2]
    files = sorted((docs / subject / chapter).glob("*.md"))
    path = docs / subject / chapter / f"{stem}.md"
    title = re.search(r"^# (.*)$", path.read_text(encoding="utf-8"), re.M).group(1)
    number = f"{int(chapter)}-{files.index(path) + 1}"
    return subject, number, title, f"{subject}/{chapter}/{stem}/"


def _related_html(page, config) -> str:
    src = page.file.src_uri
    m = re.match(r"(\d\d[a-z_]+)/\d\d/(\d\d_\d\d\d)\.md$", src)
    if not m:
        return ""
    docs = Path(config["docs_dir"])
    key = f"{m.group(1)}/{m.group(2)}"
    others = _related_index(docs).get(key, [])
    if not others:
        return ""
    # 他の分野の問題を先に，最大5つ
    others = sorted(others, key=lambda k: k.split("/")[0] == m.group(1))[:5]
    names = {slug: name for slug, name, _, _ in (*HOME_SUBJECTS, *MATH_SUBJECTS)}
    here = page.url
    items = ""
    for other in others:
        subject, number, title, url = _problem_info(docs, other)
        href = posixpath.relpath(url, here.rstrip("/") or ".") + "/"
        items += f'<li><a class="related__link" href="{href}">{title}【{names.get(subject, subject)}】</a></li>'
    return (
        '<section class="related" aria-label="関連">'
        '<span class="related__label">関連</span>'
        f'<ul class="related__list">{items}</ul></section>'
    )


def on_post_page(output, page, config):
    related = _related_html(page, config)
    if related:
        at = output.find('<nav class="page-nav"')
        if at < 0:
            at = output.rfind("</article>")
        if at >= 0:
            output = output[:at] + related + output[at:]
    # パンくずは本文の中へ移して左端をそろえる。タイトルがあればその（下線の）下，なければ本文の先頭
    nav = BREADCRUMB.search(output)
    article = output.find(ARTICLE_START, nav.end()) if nav else -1
    if article < 0:
        return output
    title_end = output.find("</h1>", article)
    at = title_end + len("</h1>") if title_end >= 0 else article + len(ARTICLE_START)
    crumb = nav.group(0).replace('class="md-path__link"', 'class="md-path__link" aria-label="トップページ"', 1)
    crumb = PATH_NAME.sub(_crumb_icon, crumb)
    return output[: nav.start()] + output[nav.end() : at] + crumb + output[at:]


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


# ---- 参考文献一覧：分野の見出しにアイコン，冒頭の「このページは何？」を薄いグレーの面で囲む ----

ICON_DIR = Path(material.__file__).parent / "templates/.icons/fontawesome/solid"
BOOK_ICONS = {
    "力学": "apple-whole",
    "電磁気学": "magnet",
    "熱力学": "temperature-half",
    "量子力学": "atom",
    "統計力学": "dice",
    "固体物性": "cube",
    "線形代数": "table-cells",
    "微分方程式": "chart-line",
    "ベクトル解析": "location-arrow",
    "積分変換": "wave-square",
    "複素関数": "infinity",
    "特殊関数・変分法": "bezier-curve",
    "確率・統計": "chart-column",
    "その他": "book",
}


def _icon(name: str) -> str:
    return re.sub(r"<!--.*?-->", "", (ICON_DIR / f"{name}.svg").read_text(encoding="utf-8"))


def _books(html: str) -> str:
    def head(m):
        title = m.group(2).strip()
        if title not in BOOK_ICONS:
            return m.group(0)
        return (f'<h2 id="{m.group(1)}" class="books-head"><span class="books-head__icon">'
                f"{_icon(BOOK_ICONS[title])}</span>{title}</h2>")

    html = re.sub(r'<h2 id="([^"]+)">(.*?)</h2>', head, html)
    intro = re.search(r'<h2 id="[^"]+">このページは何？</h2>.*?(?=<h2 )', html, re.DOTALL)
    if intro:
        html = html[: intro.start()] + f'<section class="books-intro">{intro.group(0)}</section>' + html[intro.end() :]
    return html


# ---- トップページ：分野のタイル（問題数と難易度の割合のバー），難易度の入口，運営者のカード ----

HOME_SUBJECTS = (
    ("01mechanics", "力学", "apple-whole", "運動方程式・剛体から解析力学まで"),
    ("02electromagnetism", "電磁気学", "magnet", "静電場・静磁場からマクスウェル方程式，放射まで"),
    ("03thermodynamics", "熱力学", "temperature-half", "熱力学の諸法則から熱力学関数，相転移まで"),
    ("04quantum_mechanics", "量子力学", "atom", "束縛・散乱問題から電磁場の量子化まで"),
    ("05statistical_mechanics", "統計力学", "dice", "古典・量子統計から非平衡，開放量子系まで"),
    ("06solid_state", "固体物性", "cube", "結晶構造・格子振動からバンド，磁性・超伝導まで"),
)
MATH_SUBJECTS = (
    ("07linear_algebra", "線形代数", "table-cells", "行列の計算から固有値問題・内積空間・物理への応用まで"),
    ("08differential_equations", "微分方程式", "chart-line", "1階・2階の常微分方程式から偏微分方程式，安定性まで"),
    ("09vector_analysis", "ベクトル解析", "location-arrow", "勾配・発散・回転から積分定理，曲線座標まで"),
    ("10integral_transforms", "積分変換", "wave-square", "フーリエ級数・フーリエ変換・デルタ関数・ラプラス変換"),
    ("11complex_analysis", "複素関数", "infinity", "正則関数・複素積分・留数定理と物理への応用"),
    ("12special_functions", "特殊関数・変分法", "bezier-curve", "ガンマ関数・直交多項式・ベッセル関数と変分法"),
    ("13probability_statistics", "確率・統計", "chart-column", "確率分布・極限定理・統計的推定と確率過程の入口"),
)
HOME_LEVELS = (("基本", "定期試験に出てくる程度"), ("標準", "院試のベーシックな問題"), ("発展", "やや発展的なトピック"))
BRAND_DIR = ICON_DIR.parent / "brands"


def _level_counts(docs: Path, subject: str) -> dict:
    counts = {name: 0 for name in LEVELS}
    for md in sorted((docs / subject).glob("*/*.md")):
        level = _level(md)
        for name, value in LEVELS.items():
            if value == level:
                counts[name] += 1
    return counts


def _home_heading(title: str, icon: str, id_: str = "") -> str:
    id_attr = f' id="{id_}"' if id_ else ""
    return f'<h2{id_attr} class="books-head"><span class="books-head__icon">{_icon(icon)}</span>{title}</h2>'


def _home(html: str, page, config) -> str:
    docs = Path(config["docs_dir"])
    math_subjects = [m for m in MATH_SUBJECTS if (docs / m[0]).is_dir()]
    counts = {slug: _level_counts(docs, slug) for slug, *_ in (*HOME_SUBJECTS, *math_subjects)}
    page.meta["problem_total"] = sum(sum(c.values()) for c in counts.values())

    sections = {}
    for m in re.finditer(r'<h2 id="[^"]+">(.*?)</h2>(.*?)(?=<h2 |\Z)', html, re.DOTALL):
        sections[re.sub(r"<[^>]+>", "", m.group(1)).strip()] = m.group(2)

    def _tiles(subjects):
        out = ""
        for slug, name, icon, desc in subjects:
            c = counts[slug]
            bar = "".join(
                f'<span class="home-bar__seg home-bar__seg--{i}" style="flex:{c[k]}" title="{k} {c[k]}問"></span>'
                for i, k in enumerate(LEVELS, 1)
            )
            out += (
                f'<a class="home-tile" href="{slug}/"><span class="home-tile__icon">{_icon(icon)}</span>'
                f'<span class="home-tile__body"><span class="home-tile__name">{name}<span class="home-tile__count">{sum(c.values())}問</span></span>'
                f'<span class="home-tile__desc">{desc}</span><span class="home-bar">{bar}</span></span></a>'
            )
        return out

    tiles = _tiles(HOME_SUBJECTS)
    math_tiles = _tiles(math_subjects)
    legend = '<p class="home-legend">' + "".join(
        f'<span class="home-bar__seg home-bar__seg--{i}"></span>{"★" * i} {k}' for i, k in enumerate(LEVELS, 1)
    ) + "</p>"

    levels = ""
    for i, (name, desc) in enumerate(HOME_LEVELS, 1):
        total = sum(c[name] for c in counts.values())
        levels += (
            f'<a class="home-level" href="tags/?difficulty={name}"><span class="home-level__stars">{"★" * i}'
            f'<span class="off">{"☆" * (3 - i)}</span></span><span class="home-level__name">{name}</span>'
            f'<span class="home-level__desc">{desc}</span><span class="home-level__count">{total}問</span></a>'
        )

    owner = sections.get("運営者情報・SNS", "")
    bio = re.search(r"<p>(.*?)</p>", owner, re.DOTALL)
    links = re.findall(r'<strong>(.*?)：?</strong>\s*<a href="([^"]+)">', owner)
    buttons = ""
    for label, href in links:
        icon = (BRAND_DIR / "x-twitter.svg") if "twitter" in href or "x.com" in href else (ICON_DIR / "pen-nib.svg")
        svg = re.sub(r"<!--.*?-->", "", icon.read_text(encoding="utf-8"))
        name = "X" if "twitter" in href or "x.com" in href else re.sub(r"[:：\s]", "", label)
        buttons += f'<a class="home-owner__link" href="{href}" target="_blank" rel="noopener"><span class="home-owner__icon">{svg}</span>{name}</a>'
    owner_card = (
        '<div class="home-owner"><img class="home-owner__avatar" src="assets/favicon.svg" alt="" width="64" height="64">'
        f'<div class="home-owner__body"><p class="home-owner__name">ななな２<span>なななつ</span></p>'
        f'<p class="home-owner__bio">{bio.group(1) if bio else ""}</p><p class="home-owner__links">{buttons}</p></div></div>'
    )

    news = sections.get("更新履歴", "")
    return (
        _home_heading("分野から選ぶ", "layer-group", "fields")
        + f'<h3 class="home-subhead">物理</h3><div class="home-tiles">{tiles}</div>'
        + (f'<h3 class="home-subhead">物理数学</h3><div class="home-tiles">{math_tiles}</div>' if math_tiles else "")
        + legend
        + _home_heading("難易度から選ぶ", "star")
        + f'<div class="home-levels">{levels}</div>'
        + (_home_heading("更新履歴", "clock-rotate-left") + f'<div class="home-news">{news}</div>' if news else "")
        + _home_heading("このサイトは何者？", "circle-question")
        + sections.get("このサイトは何者？", "")
        + _home_heading("重要な約束と推奨される使い方", "triangle-exclamation")
        + f'<div class="home-promise">{sections.get("重要な約束と推奨される使い方", "")}</div>'
    )
