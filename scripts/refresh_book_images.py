#!/usr/bin/env python3
"""参考文献ページ（docs/books.md）の表紙画像を，Creators API が返す公式の画像 URL に置きかえる。

    python3 scripts/refresh_book_images.py

認証情報は .env から読む（amazon_creators.py と同じ）。本を足したときや，画像が変わったときに実行し直す。
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS = ROOT / "docs/books.md"
TOOL = ROOT / "scripts/amazon_creators.py"


def main() -> int:
    text = BOOKS.read_text(encoding="utf-8")
    asins = list(dict.fromkeys(re.findall(r"amazon\.co\.jp/dp/([0-9A-Z]{10})", text)))
    urls = {}
    for i in range(0, len(asins), 10):  # getItems は1回に10件まで
        r = subprocess.run([sys.executable, str(TOOL), "get-items", *asins[i:i + 10]], capture_output=True, text=True)
        if r.returncode:
            print(r.stderr.strip(), file=sys.stderr)
            return 1
        for item in json.loads(r.stdout):
            urls[item["asin"]] = item.get("images", {}).get("primary", {}).get("large", {}).get("url")
    missing = [a for a in asins if not urls.get(a)]
    cards = text.split('<div class="book-card">')
    changed = 0
    for k in range(1, len(cards)):
        m = re.search(r"amazon\.co\.jp/dp/([0-9A-Z]{10})", cards[k])
        if m and urls.get(m.group(1)):
            new = re.sub(r'<img src="https://m\.media-amazon\.com/images/I/[^"]+"', f'<img src="{urls[m.group(1)]}"', cards[k], count=1)
            changed += new != cards[k]
            cards[k] = new
    BOOKS.write_text('<div class="book-card">'.join(cards), encoding="utf-8")
    print(f"{len(asins)} 冊を問い合わせ，{changed} 冊の画像を更新しました。" + (f" 画像なし：{missing}" if missing else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
