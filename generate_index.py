import os
import re

# 対象とする単元フォルダ（実際のフォルダ名に合わせて調整してください）
TARGET_DIRS = ["mechanics", "statistical_mechanics", "quantum_mechanics"]

for base_dir in TARGET_DIRS:
    docs_base_path = os.path.join("docs", base_dir)
    if not os.path.exists(docs_base_path):
        continue

    display_title = base_dir.capitalize()  
    pages_path = os.path.join(docs_base_path, ".pages")
    
    if os.path.exists(pages_path):
        with open(pages_path, "r", encoding="utf-8") as f:
            for line in f:
                match = re.search(r"title:\s*(.+)", line)
                if match:
                    display_title = match.group(1).strip().strip('"').strip("'")
                    break    


    # 新しく書き出す index.md の中身のベース
    content = f"# {base_dir.capitalize()} の問題一覧\n\n"
    content += "この単元に収録されている演習問題の一覧です。フォルダと.pagesファイルから自動生成されています。\n\n"
    content += '<div class="grid cards" markdown>\n\n'

    # 01, 02, 03... などのサブフォルダをループ処理
    subdirs = sorted([d for d in os.listdir(docs_base_path) if os.path.isdir(os.path.join(docs_base_path, d))])
    
    for subdir in subdirs:
        subdir_path = os.path.join(docs_base_path, subdir)
        md_files = sorted([f for f in os.listdir(subdir_path) if f.endswith(".md")])
        
        if not md_files:
            continue
            
        # ---  【ここから改良】 .pages ファイルからタイトルを取得する ---
        chapter_title = f"{subdir} 章"  # .pagesが無いか、titleが無い場合のフォールバック
        pages_file_path = os.path.join(subdir_path, ".pages")
        
        if os.path.exists(pages_file_path):
            with open(pages_file_path, "r", encoding="utf-8") as pf:
                for line in pf:
                    # 「title: 〇〇」または「title: "〇〇"」にマッチする正規表現
                    match = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", line)
                    if match:
                        chapter_title = match.group(1).strip()
                        break
        # ---  【ここまで改良】 ---
            
        # グリッドのカード（章ごと）の始まり
        content += f"-   __{chapter_title}__\n\n"
        content += "    ---\n\n"
        
        for md_file in md_files:
            # index.md自体は除外（万が一サブフォルダ内にあった場合用）
            if md_file == "index.md":
                continue
                
            file_path = os.path.join(subdir_path, md_file)
            
            # 各 md ファイルの一番最初の「# タイトル」を抜き出す
            title = md_file  # 見つからなかった場合のフォールバック
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    match = re.match(r"^#\s+(.+)$", line)
                    if match:
                        title = match.group(1).strip()
                        break
            
            # index.md から見た相対リンクを作成
            relative_link = f"{subdir}/{md_file}"
            content += f"    * [{title}]({relative_link})\n"
            
        content += "\n"  # カード間の改行

    content += "</div>\n"

    # index.md を自動生成（または上書き）
    index_path = os.path.join(docs_base_path, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f" {index_path} を自動生成しました！（.pages対応版）")