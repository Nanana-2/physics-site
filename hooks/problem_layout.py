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
    "14calculus",
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
        f'<h2 id="{heading.group(1)}"><span>{"総合問題" if _is_comprehensive(page.file.src_uri) else "問題"}</span>{_stars(page.meta)}</h2>'
        f'<div class="problem-box__body">{body}</div>'
        "</div>"
    )
    rest = html[rule.end() :]
    # 解答・解説の帯と，小問ごとの小見出し（(1) の右に細い線）
    rest = re.sub(r'<h2 id="([^"]+)">解答・解説</h2>', r'<h2 id="\1" class="solution-heading">解答・解説</h2>', rest, count=1)
    rest = re.sub(r'<h3 id="([^"]+)">', r'<h3 id="\1" class="solution-part">', rest)
    rest = _fold_answers(rest)
    head = re.sub(r"<h1 ", '<h1 class="problem-title" ', html[: heading.start()], count=1)
    # 作成中の注意書きは「Markdownでコピー」のボタンの下に置く
    notes = "".join(WIP_NOTE.findall(head))
    head = WIP_NOTE.sub("", head)
    return head + _copy_source(page) + notes + box + rest


WIP_NOTE = re.compile(r'<p class="wip-note">.*?</p>', re.DOTALL)
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


def _is_comprehensive(path: str) -> bool:
    # 総合問題はファイル名の番号を 9xx にする（<章>_910.md など）
    return re.search(r"_9\d\d$", Path(path).stem) is not None


def _copy_source(page) -> str:
    """「Markdown でコピー」用に，問題と解答の Markdown をページに埋め込む（図は「（図）」に置き換える）。"""
    title = page.title or ""
    text = re.sub(r"<figure.*?</figure>", "（図は省略）", page.markdown or "", flags=re.DOTALL)
    text = re.sub(r'<aside class="rigor-note" markdown>\s*(.*?)\s*</aside>', r"補足：\1", text, flags=re.DOTALL)
    text = re.sub(r'<div class="approach" markdown>\s*(.*?)\s*</div>', r"考え方：\1", text, flags=re.DOTALL)
    text = re.sub(r'<div class="approach-points" markdown>\s*(.*?)\s*</div>', r"性質：\n\1", text, flags=re.DOTALL)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    text = f"# {title}\n\n{text}" if not text.startswith("# ") else text
    text = text.replace("</", "<\\/")
    return (
        '<div class="page-tools">'
        '<button type="button" class="page-tools__copy" data-copy-markdown hidden>'
        '<span class="page-tools__icon" aria-hidden="true"></span><span data-copy-label>Markdownでコピー</span></button></div>'
        f'<script type="text/markdown" id="page-markdown">{text}</script>'
    )


BREADCRUMB = re.compile(r'<nav class="md-path".*?</nav>\s*', re.DOTALL)
ARTICLE_START = '<article class="md-content__inner md-typeset">'


# ---- 関連する問題：hooks/related_problems.txt のグループから，前後の問題とこの章の問題の下に並べる ----
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
        f'<span class="related__label"><span class="related__icon" aria-hidden="true">{_icon("link")}</span>関連</span>'
        f'<ul class="related__list">{items}</ul></section>'
    )


def on_post_page(output, page, config):
    related = _related_html(page, config)
    if related:
        # 次の問題とこの章の問題の下（参考文献一覧の上）に置く
        at = output.find('<nav class="page-links"')
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
    return output[: nav.start()] + output[nav.end() : at] + crumb + output[at:]


# ---- 分野別の問題一覧：章ごとのカードを目次（番号・タイトル・★）に組み替え，最初に章の目次（押すとその章へ移る）を置く ----

CHAPTER_CARD = re.compile(
    r"<li>\s*<p><strong>(\d+)\.\s*(.*?)</strong></p>\s*<hr\s*/?>\s*(?:<p>(.*?)</p>\s*)?<ul>(.*?)</ul>\s*</li>", re.DOTALL
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
    sections, index = [], []
    for number, title, note, items in CHAPTER_CARD.findall(grid.group(0)):
        links = re.findall(r'<a href="([^"]+)">(.*?)</a>', items)
        rows = "".join(
            f'<a class="toc-row" href="{href}"><span class="toc-row__num">{number}-{i}</span>'
            f'<span class="toc-row__title">{name}</span>{_stars_html(_level(base / (href.strip("/") + ".md")), "toc-row__stars")}</a>'
            for i, (href, name) in enumerate(links, 1)
        )
        sections.append(
            f'<section class="toc-chapter" id="ch{number}"><h2 class="toc-chapter__head"><span class="toc-chapter__no">{number}</span>'
            f'<span class="toc-chapter__title">{title}</span></h2>'
            + (f'<p class="wip-note">{note}</p>' if note else "")
            + f"{rows}</section>"
        )
        index.append(
            f'<a class="toc-index__link" href="#ch{number}"><span class="toc-index__no">{number}</span>'
            f'<span class="toc-index__title">{title}</span></a>'
        )
    if not sections:
        return html
    nav = '<nav class="toc-index" aria-label="章の一覧">' + "".join(index) + "</nav>"
    slug = page.file.src_uri.split("/")[0]
    # 一覧の最後：問題用紙をつくるページ（この分野を選んだ状態で開く）と参考文献一覧。問題ページの参考文献一覧と同じボタンを2列に並べる
    exam = (
        '<nav class="page-links page-links--pair" aria-label="関連ページ">'
        f'<a class="page-links__button page-links__button--print" href="../exam/?subject={slug}">'
        '<span class="page-links__label">問題用紙を<wbr>つくる</span><span class="page-links__arrow" aria-hidden="true">→</span></a>'
        '<a class="page-links__button page-links__button--books" href="../books/">'
        '<span class="page-links__label">参考文献一覧</span><span class="page-links__arrow" aria-hidden="true">→</span></a></nav>'
    )
    return html[: grid.start()] + nav + '<div class="toc">' + "".join(sections) + "</div>" + exam + html[grid.end() :]


# ---- 参考文献一覧：分野の見出しを帯にする（科目のアイコンは付けない），冒頭の「このページは何？」を薄いグレーの面で囲む ----

ICON_DIR = Path(material.__file__).parent / "templates/.icons/fontawesome/solid"
SITE_ICON_DIR = Path(__file__).resolve().parents[1] / "overrides/.icons/site"
BOOK_SUBJECTS = (
    "力学",
    "電磁気学",
    "熱力学",
    "量子力学",
    "統計力学",
    "物性物理学",
    "微積分",
    "線形代数",
    "微分方程式",
    "ベクトル解析",
    "積分変換",
    "複素関数",
    "特殊関数・変分法",
    "確率・統計",
    "その他",
)


def _icon(name: str) -> str:
    # site/ で始まる名前はサイト独自のアイコン（overrides/.icons/site/），それ以外は Font Awesome
    path = SITE_ICON_DIR / f"{name[5:]}.svg" if name.startswith("site/") else ICON_DIR / f"{name}.svg"
    return re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"))


def _books(html: str) -> str:
    def head(m):
        title = m.group(2).strip()
        if title not in BOOK_SUBJECTS:
            return m.group(0)
        return f'<h2 id="{m.group(1)}" class="books-head books-head--plain">{title}</h2>'

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
    ("06solid_state", "物性物理学", "cube", "結晶構造・格子振動からバンド，磁性・超伝導，トポロジカル物性まで"),
)
MATH_SUBJECTS = (
    ("14calculus", "微積分", "site/integral", "数列の極限・級数から1変数・多変数の微積分まで"),
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


def _home_heading(title: str, id_: str = "") -> str:
    # トップの見出しは飾りを付けず，大きな文字と短い下線だけにする（見た目は extra.css の .home-head）
    id_attr = f' id="{id_}"' if id_ else ""
    return f'<h2{id_attr} class="home-head">{title}</h2>'


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
        for slug, name, _icon_name, desc in subjects:
            c = counts[slug]
            bar = "".join(
                f'<span class="home-bar__seg home-bar__seg--{i}" style="flex:{c[k]}" title="{k} {c[k]}問"></span>'
                for i, k in enumerate(LEVELS, 1)
            )
            out += (
                f'<a class="home-tile" href="{slug}/">'
                f'<span class="home-tile__body"><span class="home-tile__name">{name}<span class="home-tile__count">{sum(c.values())}問</span></span>'
                f'<span class="home-bar">{bar}</span><span class="home-tile__desc">{desc}</span></span></a>'
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
        f'<div class="home-owner__body"><p class="home-owner__name">ななな２</p>'
        f'<p class="home-owner__bio">{bio.group(1) if bio else ""}</p><p class="home-owner__links">{buttons}</p></div></div>'
    )

    news = sections.get("更新履歴", "")
    return (
        _home_heading("分野から選ぶ", "fields")
        + f'<h3 class="home-subhead">物理</h3><div class="home-tiles">{tiles}</div>'
        + (f'<h3 class="home-subhead">物理数学</h3><div class="home-tiles">{math_tiles}</div>' if math_tiles else "")
        + legend
        + _home_heading("何のサイト？", "about")
        + sections.get("何のサイト？", "")
        # 背景の帯をもう一度見せる欄：問題を探す・問題用紙をつくる・参考文献一覧への入口（「何のサイト？」を読んだ人がそのまま次へ進めるよう，すぐ後に置く）
        + '<div class="home-band"><div class="home-tiles">'
        '<a class="home-tile" href="tags/"><span class="home-tile__body"><span class="home-tile__name">問題を探す</span>'
        '<span class="home-tile__desc">キーワードと難易度で，すべての分野から問題を絞り込みます。</span></span></a>'
        '<a class="home-tile" href="exam/"><span class="home-tile__body"><span class="home-tile__name">問題用紙をつくる</span>'
        '<span class="home-tile__desc">好きな問題を選んで，試験の形式で印刷します。</span></span></a>'
        '<a class="home-tile" href="books/"><span class="home-tile__body"><span class="home-tile__name">参考文献一覧</span>'
        '<span class="home-tile__desc">このサイトを作るにあたって参照した教科書を紹介します。</span></span></a>'
        '</div></div>'
        + _home_heading("AIの利用について", "ai")
        + sections.get("AIの利用について", "")
        + _home_heading("推奨される使い方", "usage")
        + f'<div class="home-promise">{sections.get("推奨される使い方", "")}</div>'
        + (_home_heading("更新履歴", "news") + f'<div class="home-news">{news}</div>' if news else "")
    )
