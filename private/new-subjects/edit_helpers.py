"""問題の手直し用の小さな関数（Claude 用）。"""
def rep(p,a,b):
    s=open(p).read(); assert a in s,(p,a[:80]); open(p,'w').write(s.replace(a,b,1))
def unbox(p,prefix):
    """\\finalanswer{prefix...} の囲みを外す。"""
    s=open(p).read(); key='\\finalanswer{'+prefix; j=s.find(key); assert j>=0,(p,prefix)
    k=j+13;d=1
    while d: d+={'{':1,'}':-1}.get(s[k],0); k+=1
    s=s[:j]+s[j+13:k-1]+s[k:]; open(p,'w').write(s)
def label(p,prefix,lab):
    rep(p,'\\finalanswer{'+prefix,'\\finalanswer{'+lab+prefix)
def subq(p,n,new):
    """問題文の (n) の段落を置き換える。"""
    import re
    s=open(p).read(); m=re.search(r'^\('+str(n)+r'\) .*$',s,re.M); assert m,(p,n)
    s=s[:m.start()]+f'({n}) '+new+s[m.end():]; open(p,'w').write(s)
