"""計算の別行数式の直後に，接続の言葉なしで答えの別行数式が続く箇所に「したがって，」「よって，」を入れる。
PDF原稿がある分野は，原稿の対応する箇所（答えの式の直前の数式環境の間）にも入れる。
使い方: python3 add_connectives.py [-n] file..."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from display_bigops import tex_for, ROOT

PAIR = re.compile(r'(\$\$\n(?:(?!\$\$).)*?\n\$\$\n\n)(\$\$\n((?:(?!\$\$).)*?\\finalanswer(?:(?!\$\$).)*?)\n\$\$)', re.S)
WORDS = ('したがって，', 'よって，')
TEX_START = re.compile(r'^\s*(\\\[|\\begin\{(align|equation|gather)\*?\})')
TEX_END = re.compile(r'(\\\]|\\end\{(align|equation|gather)\*?\})\s*$')

def norm(s):
    s = s.replace('\\mathrm{d}', 'd').replace('\\dfrac', '\\frac').replace('\\left', '').replace('\\right', '')
    return re.sub(r'\s|\\,|\\!|\;', '', s)

def tex_insert(tex, answer, word):
    """原稿で答えを含む数式環境を探し，直前の行も数式環境の終わりなら間に word を入れる。"""
    key = norm(answer)[:60]
    lines = tex.split('\n')
    for i, l in enumerate(lines):
        if '\\finalanswer' in l and key[:25] and norm(l).find(norm(answer.split('\n')[0])[:25]) >= 0:
            j = i
            while j >= 0 and not TEX_START.match(lines[j]): j -= 1
            if j < 0: return None
            k = j - 1
            while k >= 0 and not lines[k].strip(): k -= 1
            if k >= 0 and TEX_END.search(lines[k]):
                return '\n'.join(lines[:j] + [word] + lines[j:])
            return tex  # 既に文がある
    return None

if __name__ == '__main__':
    dry = '-n' in sys.argv
    total = 0
    for a in [x for x in sys.argv[1:] if not x.startswith('-')]:
        f = Path(a).resolve(); web = str(f.relative_to(ROOT / 'docs'))
        t = f.read_text(); n_ins = 0; answers = []
        def rep(m):
            global n_ins_g
            w = WORDS[len(answers) % 2]; answers.append((m.group(3), w))
            return m.group(1) + w + '\n\n' + m.group(2)
        new = PAIR.sub(rep, t)
        if new == t: continue
        total += len(answers)
        texs = [x for x in tex_for(web) if '-sample' not in x.parent.parent.name]
        texts = {x: x.read_text() for x in texs}
        for x in texs:
            for ans, w in answers:
                r = tex_insert(texts[x], ans, w)
                if r is None: print('TEX MISS', x.parent.parent.name, x.name, ans[:50].replace('\n', ' '))
                else: texts[x] = r
        if not dry:
            f.write_text(new)
            for x in texs: x.write_text(texts[x])
    print('inserted', total)
