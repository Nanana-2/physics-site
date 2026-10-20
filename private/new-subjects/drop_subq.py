"""問題から小問 (n) を1つ取り除き，後ろの小問の番号と本文中の参照 (k) を詰める。
使い方: python3 drop_subq.py file n [-n]   (-n は結果を表示するだけ)
取り除いた小問を参照している箇所は "REF(n)" として表示するので，手で直す。"""
import re, sys

def drop(text, n):
    head, sep, sol = text.partition('## 解答・解説')
    # 問題文：(n) の段落から次の小問または区切り線の直前まで
    m = re.search(rf'^\({n}\) ', head, re.M)
    rest = head.index('\n', m.end())  # 小問の1行目は丸ごと消す（「(4) (3) の…」のように参照で始まる場合がある）
    nxt = re.search(r'^\(\d\) |^---\s*$', head[rest:], re.M)
    head = head[:m.start()] + head[rest + nxt.start():]
    # 解答：### (n) から次の ### (k) または末尾まで
    m = re.search(rf'^### \({n}\)\s*$', sol, re.M)
    nxt = re.search(r'^### \(\d\)', sol[m.end():], re.M)
    sol = sol[:m.start()] + (sol[m.end() + nxt.start():] if nxt else '')
    body = head + sep + sol
    refs = [x.start() for x in re.finditer(rf'(?<![A-Za-z}}\\_^])\({n}\)', body)]
    # 後ろの番号を詰める（小問の行頭・見出し・本文中の参照）
    def ren(x):
        k = int(x.group(1))
        return f'({k - 1})' if k > n else x.group(0)
    body = re.sub(r'(?<![A-Za-z}\\_^])\((\d)\)', ren, body)
    return re.sub(r'\n{3,}', '\n\n', body).rstrip() + '\n', [body[max(0, r - 40):r + 20].replace('\n', ' ') for r in refs]

if __name__ == '__main__':
    f, n = sys.argv[1], int(sys.argv[2])
    new, refs = drop(open(f).read(), n)
    for r in refs: print('REF', r)
    if '-n' in sys.argv: print(new)
    else: open(f, 'w').write(new)
