# generate_local.py
from google import genai
import os
import yaml
import time
from prompt_config import get_physics_prompt  # 👈 共通プロンプトを読み込む

# ユーザーに入力してもらう
try:
    user_input = input("未作成の問題を何個一括生成しますか？ (数字を入力): ")
    MAX_GENERATE_COUNT = int(user_input)
except ValueError:
    print("有効な数字を入力してください。")
    exit(1)

DELAY_SECONDS = 10  # API制限を回避する休憩時間

# APIキーの設定
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("エラー: APIキーが設定されていません。")
    exit(1)

client = genai.Client(api_key=API_KEY)

SUBJECTS = [
    {
        "yaml_file": "curriculum_mechanics.yaml",
        "yaml_key": "mechanics",
        "output_dir": "docs/01mechanics",
        "subject_name": "力学（解析力学含む）"
    },
    {
        "yaml_file": "curriculum_quantum_mechanics.yaml",
        "yaml_key": "quantum_mechanics",
        "output_dir": "docs/04quantum_mechanics",
        "subject_name": "量子力学"
    }
]

# 未作成の問題を探索
targets = []
for subject in SUBJECTS:
    if not os.path.exists(subject["yaml_file"]):
        continue 

    with open(subject["yaml_file"], "r", encoding="utf-8") as f:
        curriculum = yaml.safe_load(f)

    for section in curriculum[subject["yaml_key"]]:
        for prob in section["problems"]:
            chapter_id = prob['id'].split('_')[0] 
            chapter_dir = os.path.join(subject["output_dir"], chapter_id)
            file_path = os.path.join(chapter_dir, f"{prob['id']}.md")
            
            # 未作成または空ファイル
            if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
                if not os.path.exists(chapter_dir):
                    os.makedirs(chapter_dir, exist_ok=True)
                    with open(os.path.join(chapter_dir, ".pages"), "w", encoding="utf-8") as pf:
                        pf.write(f"title: {section['theme']}\n")
                
                targets.append({
                    "prob": prob, "theme": section["theme"],
                    "subject_name": subject["subject_name"], "file_path": file_path
                })
                
                if len(targets) >= MAX_GENERATE_COUNT: break
        if len(targets) >= MAX_GENERATE_COUNT: break
    if len(targets) >= MAX_GENERATE_COUNT: break

if not targets:
    print("すべての問題が生成済みです。")
    exit()

print(f"\n🚀 {len(targets)} 件の問題をローカルで一括生成します。")

# ループで生成
for i, target in enumerate(targets):
    if i > 0:
        print(f"API制限回避のため {DELAY_SECONDS} 秒待機します...")
        time.sleep(DELAY_SECONDS)

    print(f"[{i+1}/{len(targets)}] {target['prob']['title']} を生成中...")
    
    # 💡 共通化されたプロンプトを呼び出す
    prompt = get_physics_prompt(target["subject_name"], target["theme"], target["prob"])

    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
    )

    with open(target["file_path"], "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f" -> 成功！ {target['file_path']} に保存しました。")

print("\n✨ すべての生成作業が完了しました！")
print("確認して問題なければ、git push してサイトに反映させてください。")
