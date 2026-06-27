# generate.py (Actions用の軽量版)
from google import genai
import os
import yaml
from prompt_config import get_physics_prompt  # 👈 共通プロンプトを読み込む

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("エラー: APIキーが設定されていません。")
    exit(1)

client = genai.Client(api_key=API_KEY)

SUBJECTS = [
    {"yaml_file": "curriculum_mechanics.yaml", "yaml_key": "mechanics", "output_dir": "docs/01mechanics", "subject_name": "力学（解析力学含む）"},
    {"yaml_file": "curriculum_quantum_mechanics.yaml", "yaml_key": "quantum_mechanics", "output_dir": "docs/04quantum_mechanics", "subject_name": "量子力学"}
]

target_problem, target_theme, target_subject_name, target_file_path = None, "", "", ""

for subject in SUBJECTS:
    if not os.path.exists(subject["yaml_file"]): continue 
    with open(subject["yaml_file"], "r", encoding="utf-8") as f:
        curriculum = yaml.safe_load(f)

    for section in curriculum[subject["yaml_key"]]:
        for prob in section["problems"]:
            chapter_id = prob['id'].split('_')[0] 
            chapter_dir = os.path.join(subject["output_dir"], chapter_id)
            file_path = os.path.join(chapter_dir, f"{prob['id']}.md")
            
            if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
                if not os.path.exists(chapter_dir):
                    os.makedirs(chapter_dir, exist_ok=True)
                    with open(os.path.join(chapter_dir, ".pages"), "w", encoding="utf-8") as pf:
                        pf.write(f"title: {section['theme']}\n")
                
                target_problem = prob
                target_theme = section["theme"]
                target_subject_name = subject["subject_name"]
                target_file_path = file_path
                break
        if target_problem: break
    if target_problem: break

if not target_problem:
    print("すべての問題が生成済みです。")
    exit()

print(f"GitHub Actions経由で「{target_problem['title']}」を自動生成します。")

# 💡 共通プロンプトを呼び出す
prompt = get_physics_prompt(target_subject_name, target_theme, target_problem)

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
)

with open(target_file_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"成功しました！: {target_file_path}")
