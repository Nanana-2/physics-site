"""aligned の外にあり，= を含まない答え（左辺がない答え）を列挙する。"""
import re,sys
for f in sys.argv[1:]:
    t=open(f).read(); i=0
    while (j:=t.find(r'\finalanswer{',i))>=0:
        k=j+13;d=1;eq=False
        while d:
            c=t[k]; d+={'{':1,'}':-1}.get(c,0)
            if c in '=<>' and d==1: eq=True
            if t[k:k+3] in (r'\le',r'\ge') or t[k:k+7]==r'\approx' or t[k:k+3]==r'\to': eq=True
            k+=1
        pre=t[max(0,j-4):j]
        if not eq and '&' not in pre:
            sec=t.rfind('### (',0,j); print(f, t[sec+4:sec+7], t[j+13:k-1][:70].replace('\n',' '))
        i=k
