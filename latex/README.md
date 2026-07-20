# PDF版のLaTeXソース

Webサイトとは分けて，問題集のPDF版を作るためのソースを置くディレクトリです。

- `common/book-style.tex`: 各分野で共通して使う書式
- `mechanics/main.tex`: 力学編の親ファイル（B5判）
- `mechanics/a4.tex`: 同じ内容をA4判で出力するための入口
- `mechanics/frontmatter/`: 「はじめに」などの前付
- `mechanics/problems/`: 各問題のLaTeX本文
- `tools/convert_problem.py`: サイトのMarkdownを問題ごとのLaTeXへ変換する補助スクリプト
- `output/pdf/`: 生成した完成PDF
- `tmp/pdfs/`: コンパイル時の中間ファイル

現時点では，力学の第1・第2章（全10問）を収録した試作版です。
