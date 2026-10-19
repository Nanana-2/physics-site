"""文体・形式の点検（Claude 用）。 python3 lint_style.py <dir or files>"""
import re,sys,glob,os
from collections import Counter
JP=re.compile(r'[぀-ヿ一-鿿]')
def files(args):
    for a in args:
        if os.path.isdir(a): yield from sorted(glob.glob(a+'/**/*.md',recursive=True))
        else: yield a
def lint(t):
    out=[]
    prob,_,sol=t.partition('## 解答・解説')
    subs=re.findall(r'^\((\d)\)',prob,re.M)
    if len(subs)>3: out.append(f'subq={len(subs)}')
    for line in re.findall(r'^\(\d\).*$',prob,re.M):
        if re.search(r'求め，|また，|示し，|確かめよ|答えよ。$',line): out.append('multi-ask')
    body=re.sub(r'<!--.*?-->','',t,flags=re.S)
    for m in re.finditer(r'\$\$(.+?)\$\$|\$([^$\n]+?)\$',body,re.S):
        if JP.search(m.group(0)): out.append('JP-in-math'); break
    inl=re.sub(r'\$\$.*?\$\$','',body,flags=re.S)
    if re.search(r'\$[^$\n]*\\(d?frac)[^$\n]*\$',inl): out.append('inline-frac')
    if re.search(r'\$[^$\n]{60,}\$',inl): out.append('long-inline')
    if '「' in re.sub(r'^# .*$','',body,flags=re.M) and re.search(r'「[^」]{1,12}」',sol): out.append('kagi')
    if re.search(r'（[^）$]*[぀-ヿ一-鿿][^）]*）',sol): out.append('paren-aside')
    if re.search(r'よく合|に戻り|に戻る|支配',body): out.append('phrase')
    return out
c=Counter(); per={}
for f in files(sys.argv[1:]):
    r=lint(open(f).read()); per[f]=r
    for x in set(r): c[x]+=1
n=len(per)
print(n,'files'); 
for k,v in c.most_common(): print(f'  {k}: {v}')
if '-v' in os.environ.get('LINTV',''): 
    for f,r in per.items():
        if r: print(f, sorted(set(r)))
