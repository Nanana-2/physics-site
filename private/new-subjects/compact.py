"""問題文と答え（finalanswer）だけを並べて表示する（点検用）。 python3 compact.py files..."""
import re,sys
def fa(s):
    out=[];i=0
    while (j:=s.find(r'\finalanswer{',i))>=0:
        k=j+13;d=1
        while d: d+={'{':1,'}':-1}.get(s[k],0);k+=1
        out.append(s[j+13:k-1]);i=k
    return out
for f in sys.argv[1:]:
    t=open(f).read(); prob,_,sol=t.partition('## 解答・解説')
    prob=re.sub(r'<!--.*?-->','[FIG]',prob,flags=re.S)
    prob=re.sub(r'^---\ntags:\n  - (\S+)\n---\n',r'[\1] ',prob)
    prob=re.sub(r'\n\s*\n','\n',prob).replace('## 問題\n','').replace('\n---','')
    print('=====',f); print(prob.strip())
    for part in re.split(r'^### ',sol,flags=re.M)[1:]:
        print('  ANS',part[:3],' | '.join(a.replace('\n',' ') for a in fa(part)))
