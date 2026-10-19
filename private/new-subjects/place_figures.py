"""docs/ の md の <!-- FIGURE ... --> を図のブロックに置き換える（Claude 用）。
    python3 place_figures.py <figure-folder-name> <md>...
問題図は <id>-p，解答図は出てくる順に <id>-s, <id>-s2, ...。依頼文は figreq/<folder>/<name>.txt に保存する。"""
import re,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
folder=sys.argv[1]
for md in sys.argv[2:]:
    p=Path(md); t=p.read_text(encoding='utf-8'); pid=p.stem; ns=[0]
    def sub(m):
        kind=m.group(1)
        if kind=='problem': name=f'{pid}-p'; alt='問題の図'
        else:
            ns[0]+=1; name=f'{pid}-s' if ns[0]==1 else f'{pid}-s{ns[0]}'; alt='解答の図'
        d=HERE/'figreq'/folder; d.mkdir(parents=True,exist_ok=True)
        (d/f'{name}.txt').write_text(m.group(0),encoding='utf-8')
        return (f'<figure class="problem-figure" markdown>\n![{alt}](../../assets/figures/{folder}/{name}-light.svg#only-light)\n'
                f'![{alt}](../../assets/figures/{folder}/{name}-dark.svg#only-dark)\n</figure>')
    t2=re.sub(r'<!-- FIGURE (problem|solution[^:]*): .*?-->',sub,t,flags=re.S)
    if t2!=t: p.write_text(t2,encoding='utf-8'); print(md, ns[0], 'solution figs')
