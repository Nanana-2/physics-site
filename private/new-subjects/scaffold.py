"""generated/<subj> を docs/<subj> に入れ，.pages と index.md を作る（Claude 用）。
    python3 scaffold.py 07linear_algebra [--copy]"""
import re,sys,shutil
from pathlib import Path
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE)); import plan
slug=sys.argv[1]; copy='--copy' in sys.argv
subj=next(s for s in plan.SUBJECTS if s[0]==slug)
dst=ROOT/'docs'/slug; dst.mkdir(exist_ok=True)
if copy:
    for f in sorted((HERE/'generated'/slug).glob('*/*.md')):
        (dst/f.parent.name).mkdir(exist_ok=True); shutil.copy(f,dst/f.parent.name/f.name)
(dst/'.pages').write_text(f'title: {subj[1]}\n',encoding='utf-8')
lines=['---',f'title: {subj[1]}の問題一覧','hero_image: assets/images/index.jpg','hide:','  - toc   # 本文が章の目次なので右のサイドバーは出さない（本文を中央に）','---','',
       f'# {subj[1]}の問題一覧','','この単元に収録されている演習問題の一覧です。','','<div class="grid cards" markdown>','']
for ci,(chapter,items) in enumerate(subj[3],1):
    cd=dst/f'{ci:02d}'
    if not cd.exists(): continue
    (cd/'.pages').write_text(f"title: '{ci}. {chapter}'\n",encoding='utf-8')
    lines+=[f'-   __{ci}. {chapter}__','','    ---','']
    for md in sorted(cd.glob('*.md')):
        t=re.search(r'^# (.+)$',md.read_text(encoding='utf-8'),re.M).group(1)
        lines.append(f'    * [{t}]({ci:02d}/{md.name})')
    lines.append('')
lines+=['</div>','']
(dst/'index.md').write_text('\n'.join(lines),encoding='utf-8')
print(slug, sum(1 for _ in dst.glob('*/*.md')),'problems')
