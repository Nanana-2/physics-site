"""TikZ の原稿から，サイトで使うライト用とダーク用の SVG を作る。

使い方:
    python3 tools/figures/build.py figures/src/complex-analysis/02_010-p.tex [...]
    python3 tools/figures/build.py --all

原稿 figures/src/<分野>/<名前>.tex から
docs/assets/figures/<分野>/<名前>-light.svg と <名前>-dark.svg を書き出す。
ダーク用は，ライト用の灰色（黒を含む）を明るさを反転した灰色に置きかえて作る。
黒は #d9dce4 になる。灰色以外の色は変えない。
必要なもの: pdflatex（TeX Live），pdftocairo（poppler）。
"""
import pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "figures" / "src"
OUT = ROOT / "docs" / "assets" / "figures"


def dark_gray(v):
    """ライトでの灰色の明るさ v（0〜1）を，ダークでの明るさに変える。"""
    if v <= 0.001:
        return "#d9dce4"
    w = max(0.0, min(1.0, 0.85 - 0.77 * v))
    h = round(w * 255)
    return "#{0:02x}{0:02x}{0:02x}".format(h)


def to_dark(svg):
    def rep(m):
        r, g, b = (float(x) for x in m.groups())
        if abs(r - g) < 0.5 and abs(g - b) < 0.5:
            return dark_gray(r / 100)
        return m.group(0)
    return re.sub(r"rgb\(([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)%\)", rep, svg)


def build(tex):
    tex = pathlib.Path(tex).resolve()
    rel = tex.relative_to(SRC)
    dest = OUT / rel.parent
    dest.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as d:
        shutil.copy(tex, d)
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                           cwd=d, capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stdout[-2000:])
        pdf = pathlib.Path(d) / (tex.stem + ".pdf")
        light = dest / (tex.stem + "-light.svg")
        subprocess.run(["pdftocairo", "-svg", str(pdf), str(light)], check=True)
    svg = light.read_text()
    (dest / (tex.stem + "-dark.svg")).write_text(to_dark(svg))
    print(rel, "->", light.relative_to(ROOT))


if __name__ == "__main__":
    args = sys.argv[1:]
    files = sorted(SRC.rglob("*.tex")) if args == ["--all"] else args
    for f in files:
        build(f)
