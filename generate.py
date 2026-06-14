import google.generativeai as genai
import os
import yaml

# ==========================================
# 1. APIキーの設定（※絶対にGitHubに公開しないこと！）
# ==========================================
API_KEY = "新しく取得したAPIキーをここに貼る"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3.5-flash')

# ==========================================
# 2. 管理する分野のリスト（ここを増やすだけで全分野対応）
# ==========================================
SUBJECTS = [
    {
        "yaml_file": "curriculum_mechanics.yaml",
        "yaml_key": "mechanics",
        "output_dir": "docs/mechanics",
        "subject_name": "力学（解析力学含む）"
    },
    {
        "yaml_file": "curriculum_em.yaml",
        "yaml_key": "electromagnetism",
        "output_dir": "docs/electromagnetism",
        "subject_name": "電磁気学"
    },
    # 熱力学などを作ったら、ここにブロックを追加するだけでOK
]

# ==========================================
# 3. 全分野を横断して未作成の「空席」を探す
# ==========================================
target_problem = None
target_theme = ""
target_subject_name = ""
target_file_path = ""

for subject in SUBJECTS:
    # その分野のYAMLファイルがまだ存在しなければスキップ
    if not os.path.exists(subject["yaml_file"]):
        continue 

    with open(subject["yaml_file"], "r", encoding="utf-8") as f:
        curriculum = yaml.safe_load(f)

    # 保存先フォルダが無ければ作る
    os.makedirs(subject["output_dir"], exist_ok=True)

    for section in curriculum[subject["yaml_key"]]:
        for prob in section["problems"]:
            file_name = f"{prob['id']}.md"
            file_path = os.path.join(subject["output_dir"], file_name)
            
            # ファイルがまだ存在しない場合、これを今回の生成ターゲットにする
            if not os.path.exists(file_path):
                target_problem = prob
                target_theme = section["theme"]
                target_subject_name = subject["subject_name"]
                target_file_path = file_path
                break # 1つ見つけたら探索終了
                
        if target_problem:
            break # 外側のループも抜ける
            
    if target_problem:
        break # 分野のループも抜ける

# すべての問題が完成している場合
if not target_problem:
    print("✨ すべての分野でカリキュラム内の問題が生成済みです！")
    exit()

print(f"🔍 未作成の問題を発見しました: [{target_subject_name}] {target_problem['id']}: {target_problem['title']}")
print("Geminiが指定された条件で問題を執筆中です...（数秒〜十数秒かかります）")

# ==========================================
# 4. AIへの指示（プロンプトの構築）
# ==========================================
prompt = f"""
以下の条件に従って，学生向けの物理の問題と解説を作成してください。

【設定パラメータ】
- 分野：{target_subject_name}
- テーマ：{target_theme}
- タイトル：{target_problem['title']}
- 難易度：{target_problem['difficulty']}
- 問題の設定・条件：{target_problem['setup']}

【出力要件（厳守）】
1. メタデータ：ファイルの先頭に、必ず以下の形式で難易度タグ（Frontmatter）を出力すること。
---
tags:
  - {target_problem['difficulty']}
---
2. ストーリー性：単なる数式処理ではなく，指定された設定に基づき，具体的な物理現象を解き明かしていくストーリー仕立ての構成にすること。
3. 誘導形式：問題は (1), (2), (3)... と順を追って誘導する形式にすること。前の小問の結果を使って次のステップへ進む論理的な流れを作ること。
4. 形式：数式はLaTeX形式（$$ または $）を使用し出力はすべてMarkdown形式にすること。
5. 図の不使用：図を用いず、文章のみで系の設定（配置、座標系の定義、力の向きなど）が学習者に100%誤解なく伝わるように厳密に記述すること。
6. 数式の改行：複数行の数式（align環境など）で改行を行う場合は、Markdownの干渉を防ぐため必ず `\\\\` （バックスラッシュ4つ）を使用すること。
7. 余計な挨拶や説明は一切省き、Markdownのテキストのみを直接出力してください。句読点は「。」「，」を利用すること。

【出力フォーマット】
---
tags:
  - {target_problem['difficulty']}
---

# {target_problem['title']}

## 問題
（具体的な物理系の設定と導入文）
(1) ...
(2) ...

---

## 解説
（各小問の解答と、それが意味する物理的な解釈を詳細に記述）
"""

# ==========================================
# 5. 問題の自動生成と保存
# ==========================================
response = model.generate_content(prompt)
generated_text = response.text

with open(target_file_path, "w", encoding="utf-8") as f:
    f.write(generated_text)

print(f"成功！ 新しい問題が {target_file_path} に保存されました！")