"""aligned の中の「&= \\finalanswer{X=Y}」を「&= \\finalanswer{Y}」にする（左辺の重複を消す）。"""
import re,sys
def fix(t):
    out=[];i=0
    pat=re.compile(r'&\s*=\s*\\finalanswer\{')
    while (m:=pat.search(t,i)):
        out.append(t[i:m.end()]); k=m.end(); d=1; j=k; eq=None
        while d:
            c=t[j]
            if c=='{': d+=1
            elif c=='}': d-=1
            elif c=='=' and d==1 and eq is None and t[j-1] not in '<>!\\': eq=j
            j+=1
        body=t[k:j-1]
        if eq is not None and not re.search(r'\\(le|ge|ne|approx)',t[k:eq]):
            body=t[eq+1:j-1].lstrip()
        out.append(body+'}'); i=j
    out.append(t[i:]); return ''.join(out)
for f in sys.argv[1:]:
    s=open(f).read(); n=fix(s)
    if n!=s: open(f,'w').write(n); print('fixed',f)
