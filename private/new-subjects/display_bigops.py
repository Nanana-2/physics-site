"""文中の ∫・Σ・lim の扱いをそろえる。
- 長い ∫/Σ を含む文中の数式は別行の数式に出す。
- 残った文中の Σ・Π・lim には \\displaystyle を付ける。∫ はそのまま。
- PDF原稿がある分野（力学・電磁気・熱・量子・統計）は，対応する原稿の $X$ も同じように直す（別行は \\[X\\]）。
使い方: python3 display_bigops.py [-n] file...   (-n は変更の表示のみ)"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJ = {"01mechanics": "mechanics", "02electromagnetism": "electromagnetism", "03thermodynamics": "thermodynamics",
        "04quantum_mechanics": "quantum-mechanics", "05statistical_mechanics": "statistical-mechanics"}
INL = re.compile(r'(?<![$\\])\$([^$\n]+)\$(?!\$)')
BIG = re.compile(r'\\(int|oint|sum)(?![a-zA-Z])')
DSOP = re.compile(r'\\(sum|prod|lim)(?![a-zA-Z])')


def visible_len(b):
    b = re.sub(r'\\(mathrm|operatorname|boldsymbol|left|right|,|;|!|quad|qquad)', '', b)
    return len(re.sub(r'\s', '', b))


def want_display(line, m):
    b = m.group(1)
    if not BIG.search(b) or 'finalanswer' in b: return False
    if not re.search(r'=|\\le|\\ge|<|>|\\approx', b): return False
    if visible_len(b) < 28: return False
    pre, post = line[:m.start()], line[m.end():]
    if re.match(r'^\s*(\(\d\)\s*)?$', pre): return False          # 行頭・小問番号の直後
    if pre.rstrip().endswith(('（', '(')): return False
    if post[:1] in ('，', '。', '、', '）', ')', '$', ',', '.', '（') or not post.strip(): return False
    if line.lstrip().startswith(('-', '|', '#', '<', '!', '\\item')): return False
    return True


def ds(b):
    if '\\displaystyle' in b or not DSOP.search(b): return b
    return '\\displaystyle ' + b


def process(t):
    """Web 版の本文を直す。戻り値は (新しい本文, 別行にした式のリスト, displaystyle を付けた式のリスト)。"""
    shown, styled = [], []
    def sty(x):
        b = x.group(1); nb = ds(b)
        if nb != b: styled.append(b)
        return '$' + nb + '$'
    parts = re.split(r'(\$\$.*?\$\$)', t, flags=re.S)
    out = []
    for i, pt in enumerate(parts):
        if i % 2: out.append(pt); continue
        nl = []
        for line in pt.split('\n'):
            while True:
                m = next((mm for mm in INL.finditer(line) if want_display(line, mm)), None)
                if not m: break
                pre, post = line[:m.start()].rstrip(), line[m.end():].lstrip()
                body = m.group(1).strip().replace('\\displaystyle', '').strip()
                shown.append(m.group(1))
                nl += [INL.sub(sty, pre), '', '$$', body, '$$', '']
                line = post
            nl.append(INL.sub(sty, line))
        out.append('\n'.join(nl))
    return ''.join(out), shown, styled


def tex_for(web):
    subj = SUBJ.get(web.split('/')[0])
    if not subj: return []
    md = ROOT / 'docs' / web
    return [f for f in (ROOT / 'private/pdf-books/source').glob(f'{subj}-*/problems/*.tex')
            if re.search(r'Web source: \S*docs/' + re.escape(web) + r'\s', f.read_text())
            or (f.stem == md.stem and 'Web source:' not in f.read_text())]


if __name__ == '__main__':
    dry = '-n' in sys.argv
    for a in [x for x in sys.argv[1:] if not x.startswith('-')]:
        f = Path(a).resolve(); web = str(f.relative_to(ROOT / 'docs'))
        t = f.read_text(); n, shown, styled = process(t)
        if n == t: continue
        texs = [x for x in tex_for(web) if '-sample' not in x.parent.parent.name]
        texts = {x: x.read_text() for x in texs}
        def norm(s):
            s = s.replace('\\mathrm{d}', 'd').replace('\\displaystyle', '').replace('\\dfrac', '\\frac').replace('\\tfrac', '\\frac').replace('\\left', '').replace('\\right', '')
            return re.sub(r'\s|\\,|\\!|\\;', '', s)
        def find(s, b):
            o = '$' + b + '$'
            if o in s: return o
            nb = norm(b)
            for m in INL.finditer(s):
                if norm(m.group(1)) == nb: return m.group(0)
            return None
        for x in texs:
            s = texts[x]
            for b in shown:
                o = find(s, b)
                if o: s = s.replace(o, '\n\\[\n' + o[1:-1].replace('\\displaystyle', '').strip() + '\n\\]\n', 1)
                else: print('TEX MISS(display)', x.parent.parent.name, x.name, b[:60])
            for b in styled:
                o = find(s, b)
                if o: s = s.replace(o, '$\\displaystyle ' + o[1:-1] + '$')
                else: print('TEX MISS(style)', x.parent.parent.name, x.name, b[:60])
            texts[x] = s
        print(f'{web}: display {len(shown)}, displaystyle {len(styled)}, tex {len(texs)}')
        if not dry:
            f.write_text(n)
            for x in texs: x.write_text(texts[x])
