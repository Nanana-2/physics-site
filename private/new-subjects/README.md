# 新分野（固体物性・物理数学7分野）の作り方

## 流れ（共同作業）
1. **問題の案**：`PROPOSAL.md`（`plan.py` から自動生成）。問題を足す・消すときは `plan.py` を直して `python3 plan.py`。
2. **生成（オーナー）**：`prompts/batch_XX.md` を1ファイルずつ丸ごと別の AI（Claude / Gemini）に貼る。返ってきた回答を `outputs/batch_XX.md` に保存する。一覧は `prompts/README.md`。
3. **取り込み・点検（Claude）**：`python3 import_outputs.py outputs/batch_XX.md` で1問1ファイルに分けて `generated/` に置き，形式の問題を一覧にする。図の依頼は `generated/FIGURES.md` に集まる。
4. **図（Claude）**：図の依頼を読んで TikZ で作図（`output/pdf/figures-work/` の流れ）。
5. **校閲（Codex → Claude）**：既存分野と同じ `private/pdf-books/proofreading/` の流れ。
6. **サイトへ（Claude）**：`docs/` に入れ，タブ・フッター・トップのタイル・検索の索引・PDF 原稿を追加。

## 決めること（オーナー）
- メニューの並べ方：物理数学の7分野をそのままタブに並べるとタブが13個になる。「物理数学」で1つにまとめて中で7分野を選ぶ形も検討。
