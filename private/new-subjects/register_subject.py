"""物理数学の分野をサイトに載せる（Claude 用）。 python3 register_subject.py 07linear_algebra
docs/.pages の「物理数学」に追加し，docs/physmath.md の一覧と問題を探すページのボタンを作り直す。"""
import json,re,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]; DOCS=ROOT/'docs'
MATH=json.load(open(HERE/'math_subjects.json'))
live=[m for m in MATH if (DOCS/m[0]).is_dir()]
# .pages
pages=(DOCS/'.pages').read_text(encoding='utf-8')
block='  - 物理数学:\n    - physmath.md\n'+''.join(f'    - {m[0]}\n' for m in live)
pages=re.sub(r'  - 物理数学:\n(    - .*\n)*','',pages)
pages=pages.replace('  - 06solid_state\n','  - 06solid_state\n'+block)
(DOCS/'.pages').write_text(pages,encoding='utf-8')
# landing page
lines=['---','title: 物理数学の問題一覧','hero_image: assets/images/index.jpg','hide:','  - toc','---','','# 物理数学の問題一覧','',
       '物理を学ぶときに使う数学の演習問題です。分野を選んでください。','','<div class="grid cards" markdown>','']
for slug,name,icon,_,desc in live:
    n=len(list((DOCS/slug).glob('*/*.md')))
    code=icon.replace('/','-') if icon.startswith('site/') else f'fontawesome-solid-{icon}'
    lines+=[f'-   :{code}: __{name}__（{n}問）','','    ---','',f'    {desc}','',f'    [{name}の問題一覧へ]({slug}/index.md)','']
lines+=['</div>','']
(DOCS/'physmath.md').write_text('\n'.join(lines),encoding='utf-8')
# finder buttons
tags=(DOCS/'tags.md').read_text(encoding='utf-8')
tags=re.sub(r'    <button type="button" class="finder__subject finder__subject--1[0-9][a-z_]+".*\n|    <button type="button" class="finder__subject finder__subject--0[7-9][a-z_]+".*\n','',tags)
anchor=re.search(r'data-subject="06solid_state">[^<]*</button>\n',tags).group(0)
tags=tags.replace(anchor,anchor+''.join(f'    <button type="button" class="finder__subject finder__subject--{m[0]}" data-subject="{m[0]}">{m[1]}</button>\n' for m in live))
(DOCS/'tags.md').write_text(tags,encoding='utf-8')
print('live:',[m[1] for m in live])
