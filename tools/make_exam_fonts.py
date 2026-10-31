"""問題の印刷ページ（docs/exam/print/）で使う原ノ味フォントを，使う文字だけに絞って woff2 にする。

原ノ味フォントは https://github.com/trueroad/HaranoAjiFonts から
HaranoAjiMincho-Regular.otf と HaranoAjiGothic-Regular.otf を取ってきて，そのフォルダを渡す。

    pip install fonttools brotli
    python3 tools/make_exam_fonts.py <原ノ味フォントのフォルダ>

残す文字は，JIS 第1水準の漢字・かな・記号と，問題ファイル（docs/0*/，docs/1*/）に出てくる文字。
新しい問題で第2水準の漢字などが増えたら，もう一度実行する。
"""

import sys
from pathlib import Path

from fontTools import subset

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "exam" / "print" / "fonts"
FONTS = {
    "HaranoAjiMincho-Regular.otf": "HaranoAjiMincho-Regular.woff2",
    "HaranoAjiGothic-Regular.otf": "HaranoAjiGothic-Regular.woff2",
}


def _jis_level1() -> set:
    """EUC-JP の 1〜47 区（記号・英数・かな・第1水準漢字）の文字。"""
    chars = set()
    for row in range(0xA1, 0xD0):
        for cell in range(0xA1, 0xFF):
            try:
                chars.add(bytes([row, cell]).decode("euc_jp"))
            except UnicodeDecodeError:
                pass
    return chars


def _used() -> set:
    chars = set()
    for md in ROOT.joinpath("docs").glob("[01]*/**/*.md"):
        chars.update(md.read_text(encoding="utf-8"))
    return chars


def main(src: Path) -> None:
    text = _jis_level1() | _used() | {chr(c) for c in range(0x20, 0x7F)}
    text = "".join(sorted(c for c in text if c.isprintable() or c == "\u3000"))  # 全角スペースは isprintable() が偽になる
    OUT.mkdir(parents=True, exist_ok=True)
    for name, out in FONTS.items():
        options = subset.Options()
        options.flavor = "woff2"
        options.layout_features = ["*"]
        options.name_IDs = ["*"]
        font = subset.load_font(str(src / name), options)
        subsetter = subset.Subsetter(options)
        subsetter.populate(text=text)
        subsetter.subset(font)
        subset.save_font(font, str(OUT / out), options)
        print(out, (OUT / out).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
