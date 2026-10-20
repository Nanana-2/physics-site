"""文中の数式（$...$）の \\frac を \\dfrac にする。上付き・下付きの中と，分数の分子・分母の中は \\frac のまま。
使い方: python3 inline_dfrac.py [-n] file..."""
import re, sys
dry = '-n' in sys.argv


def fix_math(m):
    s = m.group(0); out = []; stack = []; i = 0
    pending = []  # (深さ, 残りの引数の数)：直前の分数がまだ受け取っていない引数
    while i < len(s):
        if s.startswith('\\frac', i) and not s[i + 5:i + 6].isalpha():
            out.append('\\frac' if any(stack) else '\\dfrac')
            pending.append([len(stack), 2]); i += 5; continue
        c = s[i]
        if c == '{':
            arg = bool(pending) and pending[-1][0] == len(stack)
            if arg:
                pending[-1][1] -= 1
                if pending[-1][1] == 0: pending.pop()
            stack.append(arg or (i > 0 and s[i - 1] in '^_') or (bool(stack) and stack[-1]))
        elif c == '}' and stack:
            stack.pop()
        out.append(c); i += 1
    return ''.join(out)


def fix(t):
    parts = re.split(r'(\$\$.*?\$\$|<!--.*?-->)', t, flags=re.S)
    for k in range(0, len(parts), 2):
        parts[k] = re.sub(r'(?<!\$)\$[^$\n]+\$', fix_math, parts[k])
    return ''.join(parts)


for f in [a for a in sys.argv[1:] if a != '-n']:
    t = open(f).read(); n = fix(t)
    if n != t:
        print(f, n.count('\\dfrac') - t.count('\\dfrac'))
        if not dry: open(f, 'w').write(n)
