from google import genai
import os
import yaml

# ==========================================
# 1. APIキーの設定（環境変数から安全に取得）
# ==========================================
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("エラー: APIキーが設定されていません。")
    exit(1)

client = genai.Client(api_key=API_KEY)



# ==========================================
# 2. 管理する分野のリスト
# ==========================================
SUBJECTS = [
    {
        "yaml_file": "curriculum_mechanics.yaml",
        "yaml_key": "mechanics",
        "output_dir": "docs/mechanics",
        "subject_name": "力学（解析力学含む）"
    }
]

# ==========================================
# 3. 全分野を横断して未作成の「空席」を探す
# ==========================================
target_problem = None
target_theme = ""
target_subject_name = ""
target_file_path = ""

for subject in SUBJECTS:
    if not os.path.exists(subject["yaml_file"]):
        continue 

    with open(subject["yaml_file"], "r", encoding="utf-8") as f:
        curriculum = yaml.safe_load(f)

    os.makedirs(subject["output_dir"], exist_ok=True)

    for section in curriculum[subject["yaml_key"]]:
        for prob in section["problems"]:
            # --- ★YAMLのID（01_010）から、フォルダ名（01）を正確に取得 ---
            chapter_id = prob['id'].split('_')[0] 
            chapter_dir = os.path.join(subject["output_dir"], chapter_id)
            
            file_name = f"{prob['id']}.md"
            file_path = os.path.join(chapter_dir, file_name)
            
            if not os.path.exists(file_path):
                # フォルダがない場合は作成し、.pages も自動生成
                if not os.path.exists(chapter_dir):
                    os.makedirs(chapter_dir, exist_ok=True)
                    
                    pages_path = os.path.join(chapter_dir, ".pages")
                    with open(pages_path, "w", encoding="utf-8") as pf:
                        pf.write(f"title: {section['theme']}\n")
                
                target_problem = prob
                target_theme = section["theme"]
                target_subject_name = subject["subject_name"]
                target_file_path = file_path
                break
                
        if target_problem:
            break
            
    if target_problem:
        break

if not target_problem:
    print("✨ すべての分野でカリキュラム内の問題が生成済みです！")
    exit()

# ==========================================
# 4. AIへの指示（プロンプトの構築）
# ==========================================
prompt = f"""
以下の条件に従って，大学生向けの物理の問題と解説を作成してください。

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
2. ストーリー性：単なる数式処理ではなく，指定された設定に基づき，具体的な物理現象を一連の流れを持って解き進める構成にすること。
3. 誘導形式：問題は (1), (2), (3)... と順を追って誘導する形式にすること。前の小問の結果を使って次のステップへ進む論理的な流れを作ること。

4. 数式のフォーマット（超重要）：
   - 文中の短い数式（インライン）は `$F=ma$` のように `$` で囲むこと。
   - 運動方程式の立式，重要な導出ステップ，最終的な解答などの「独立した数式（ディスプレイ数式）」は，必ず以下のように `$$` を単独の行に置き，改行して数式を挟むこと。
     （良い例）
     文章...
     $$
     F = ma
     $$
     文章...
   - `$$F=ma$$` のように1行にまとめて出力することは絶対に避けてください。
   - 複数行の数式（align環境など）で改行を行う場合は，Markdownの干渉を防ぐため必ず `\\\\` （バックスラッシュ4つ）を使用すること。

5. 図の不使用：図を用いず，文章のみで系の設定（配置，座標系の定義，力の向きなど）が学習者に100%誤解なく伝わるように厳密に記述すること。
6. 余計な挨拶や説明は一切省き，Markdownのテキストのみを直接出力してください。句読点は「。」「，」を利用し，「、」を用いないこと。問題文は常態（である調），解答は敬体（ですます調）で丁寧な説明を加えつつも簡潔に記述すること。
7. 問題文と解説の両方において「」や（）といった括弧類を多用しないこと。特に問題文では、括弧を使わずに文章だけで条件や設定を伝える工夫をしてください。

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
# 5. 問題の自動生成と保存（最新SDKでの書き方）
# ==========================================
response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
)

with open(target_file_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"成功！ 新しい問題が {target_file_path} に保存されました！")