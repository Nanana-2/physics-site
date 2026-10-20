"""式のすぐ後に置く「となります。」が同じ小問の中で続くとき，2回目以降を「です。」「が得られます。」に変えて単調さを減らす。
Web 版（$$ の後）と PDF 原稿（\\] や \\end{equation*} の後）の両方に当てる。"""
import re, glob
ALT = ['となります。', 'です。', 'となります。', 'が得られます。']

def vary(text, is_tex):
    lines = text.split('\n'); count = 0; n = 0
    for i, l in enumerate(lines):
        if re.match(r'^#{2,3} |\\item|\\begin\{(mondai|kaitou)', l):
            count = 0
        if not l.startswith('となります。'):
            continue
        # 直前の空でない行が数式の終わりであること
        j = i - 1
        while j >= 0 and not lines[j].strip(): j -= 1
        prev = lines[j].strip() if j >= 0 else ''
        if not (prev == '$$' or (is_tex and re.search(r'(\\\]|\\end\{(align|equation|gather)\*?\})$', prev))):
            continue
        new = ALT[count % len(ALT)]
        if new != 'となります。':
            lines[i] = new + l[len('となります。'):]; n += 1
        count += 1
    return '\n'.join(lines), n

import sys
# 2回当てると次の「となります」がまた変わるので，必ず対象のファイルを指定して1回だけ当てる
args = sys.argv[1:]
if not args:
    sys.exit('usage: python3 vary_endings.py file...  (同じファイルに2回当てないこと)')
tot = 0
for f in args:
    t = open(f).read(); u, n = vary(t, f.endswith('.tex'))
    if n: open(f, 'w').write(u); tot += n
print('changed', tot)
