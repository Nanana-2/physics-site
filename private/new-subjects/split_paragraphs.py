"""解説の長い段落（3文以上で長いもの）を，2文ずつの段落に分ける（スマホで読みやすくするため）。Web 版のみ。
使い方: python3 split_paragraphs.py [-n] file..."""
import re, sys
dry = '-n' in sys.argv
INL = re.compile(r'\$[^$\n]+\$')

def vis_len(s):
    return len(INL.sub(lambda m: 'x' * max(1, len(m.group(0)) // 3), s))

def split_par(p):
    if vis_len(p) < 110: return p
    # 文の区切り：「。」の直後（閉じ括弧が続く場合はその後）
    parts, cur, i = [], '', 0
    tokens = re.split(r'(\$[^$\n]+\$)', p)
    buf = ''
    for k, tk in enumerate(tokens):
        if k % 2: buf += tk; continue
        for ch in tk:
            buf += ch
            if ch == '。':
                parts.append(buf); buf = ''
    if buf.strip(): parts.append(buf)
    if len(parts) < 3: return p
    out = []
    for j in range(0, len(parts), 2):
        out.append(''.join(parts[j:j + 2]).strip())
    # 最後が1文だけで短いときは前に戻す
    if len(out) > 1 and vis_len(out[-1]) < 25:
        last = out.pop(); out[-1] += last
    return '\n\n'.join(out)

n = 0
for f in [a for a in sys.argv[1:] if not a.startswith('-')]:
    t = open(f).read()
    head, sep, sol = t.partition('## 解答・解説')
    if not sep: continue
    chunks = re.split(r'(\$\$.*?\$\$|<[^>\n]*>.*?</[a-z]+>)', sol, flags=re.S)
    for i in range(0, len(chunks), 2):
        paras = chunks[i].split('\n\n')
        for k, p in enumerate(paras):
            s = p.strip('\n')
            if not s or s.startswith(('#', '|', '-', '*', '<', '!', '$', '(')) or '\n' in s: continue
            q = split_par(s)
            if q != s:
                paras[k] = p.replace(s, q); n += 1
        chunks[i] = '\n\n'.join(paras)
    new = head + sep + ''.join(chunks)
    if new != t and not dry: open(f, 'w').write(new)
print('split paragraphs', n)
