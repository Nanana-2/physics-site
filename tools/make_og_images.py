"""SNS でシェアしたときのカード画像（OGP 画像，1200×630）を問題ごとに作る。

    python3 tools/make_og_images.py

docs/assets/og/<分野>/<章>/<問題>.png と，問題以外のページ用の docs/assets/og/default.png を書き出す。
紺の背景にロゴ・分野と章・問題名・難易度の★。描画には PyMuPDF（tmp/pdfdeps にある fitz）を使う。
問題を追加・改題したら実行し直す。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tmp/pdfdeps"))
import fitz  # noqa: E402
import yaml  # noqa: E402

DOCS = ROOT / "docs"
OUT = DOCS / "assets/og"
SUBJECTS = {
    "01mechanics": "力学",
    "02electromagnetism": "電磁気学",
    "03thermodynamics": "熱力学",
    "04quantum_mechanics": "量子力学",
    "05statistical_mechanics": "統計力学",
    "06solid_state": "固体物性",
    "07linear_algebra": "線形代数",
    "08differential_equations": "微分方程式",
    "09vector_analysis": "ベクトル解析",
    "10integral_transforms": "積分変換",
    "11complex_analysis": "複素関数",
    "12special_functions": "特殊関数・変分法",
    "13probability_statistics": "確率・統計",
}
LEVELS = {"基本": 1, "標準": 2, "発展": 3}
W, H = 1200, 630
NAVY, DARK, WHITE, STAR = (0x17 / 255, 0x1D / 255, 0x3B / 255), (0x0D / 255, 0x11 / 255, 0x26 / 255), (1, 1, 1), (1, 0xD6 / 255, 0x0A / 255)
LOGO = fitz.open(str(DOCS / "assets/logo.svg"))
LOGO_PDF = fitz.open("pdf", LOGO.convert_to_pdf())


def _meta(md: Path):
    text = md.read_text(encoding="utf-8")
    m = re.match(r"---\s*\n(.*?)\n---", text, re.DOTALL)
    meta = yaml.safe_load(m.group(1)) if m else {}
    title = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE).group(1)
    tags = meta.get("tags") or []
    return title, next((LEVELS[t] for t in tags if t in LEVELS), 0)


def _chapter_title(subject: str, chapter: str) -> str:
    pages = DOCS / subject / chapter / ".pages"
    if pages.exists():
        data = yaml.safe_load(pages.read_text(encoding="utf-8")) or {}
        return str(data.get("title", chapter))
    return chapter


def _wrap(text: str, width: int) -> list:
    return [text[i : i + width] for i in range(0, len(text), width)]


def _card(path: Path, title: str, where: str, level: int, number: str = "") -> None:
    doc = fitz.open()
    page = doc.new_page(width=W, height=H)
    page.draw_rect(page.rect, color=None, fill=NAVY)
    page.draw_rect(fitz.Rect(0, H - 70, W, H), color=None, fill=DARK)
    page.draw_rect(fitz.Rect(0, H - 76, W, H - 70), color=None, fill=STAR)
    page.show_pdf_page(fitz.Rect(70, 60, 170, 160), LOGO_PDF, 0)
    page.insert_text((190, 125), "大学物理の問題集", fontsize=34, fontname="japan", color=WHITE)
    y = 250
    if where:
        page.insert_text((80, y), where, fontsize=30, fontname="japan", color=(0.78, 0.82, 0.95))
        if number:
            x = 80 + fitz.get_text_length(where, fontname="japan", fontsize=30) + 24
            page.insert_text((x, y), number, fontsize=30, fontname="helv", color=STAR)
        y += 80
    for line in _wrap(title, 17)[:2]:
        page.insert_text((80, y), line, fontsize=60, fontname="japan", color=WHITE)
        y += 82
    if level:
        page.insert_text((80, y + 10), "★" * level, fontsize=44, fontname="japan", color=STAR)
        page.insert_text((80 + 46 * level, y + 10), "☆" * (3 - level), fontsize=44, fontname="japan", color=(0.45, 0.5, 0.65))
    page.insert_text((80, H - 25), "nanana-2.github.io/physics-site", fontsize=24, fontname="helv", color=(0.7, 0.74, 0.86))
    path.parent.mkdir(parents=True, exist_ok=True)
    page.get_pixmap(dpi=72).save(str(path))


def main() -> None:
    _card(OUT / "default.png", "物理の問題をたくさん見よう！", "力学から統計力学まで", 0)
    count = 0
    for subject, name in SUBJECTS.items():
        if not (DOCS / subject).is_dir():
            continue
        for chapter_dir in sorted(p for p in (DOCS / subject).iterdir() if p.is_dir()):
            files = sorted(chapter_dir.glob("*.md"))
            chapter = _chapter_title(subject, chapter_dir.name)
            chapter_no = re.match(r"\d+", chapter)
            for i, md in enumerate(files, 1):
                title, level = _meta(md)
                number = f"{chapter_no.group(0)}-{i}" if chapter_no else ""
                chapter_name = re.sub(r"^\d+\.\s*", "", chapter)
                _card(OUT / subject / chapter_dir.name / f"{md.stem}.png", title, f"{name}｜{chapter_name}", level, number)
                count += 1
    print(f"{count} problem cards + default")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        _card(Path(sys.argv[2]), "斜面上の束縛運動と摩擦", "力学｜運動方程式と力学の基本", 1, "2-1")
    else:
        main()
