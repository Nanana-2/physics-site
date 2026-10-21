import re,glob,sys
subj=sys.argv[1]
def vis(s): return len(re.sub(r'X','xx',s))
out=[]
for f in sorted(glob.glob(f'docs/{subj}/*/[0-9]*.md')):
    t=open(f).read().split('## 解答・解説',1)[-1]
    t=re.sub(r'<div class="approach".*?</div>|<aside.*?</aside>|<!--.*?-->|<figure.*?</figure>','',t,flags=re.S)
    t=re.sub(r'\$\$.*?\$\$','\n',t,flags=re.S)
    for para in t.split('\n'):
        p=para.strip()
        if not p or p.startswith('#') or p.startswith('|'): continue
        p=re.sub(r'\$[^$]*\$','X',p)
        for s in re.findall(r'[^。]+。',p):
            flags=[]
            m=re.search(r'(は|が)，',s)
            head=s[:m.start()] if m else ''
            if m and vis(head)>=28: flags.append('HEAVY')
            if s.count('，')>=2: flags.append('COMMA')
            if re.search(r'[^，]{3,}が，[^。]*が[^。]{0,25}(出ます|わかります|求まります|得られます)',s): flags.append('PACK')
            if re.search(r'点が[^。]{0,15}(違い|特徴|ポイント)です|ことが[^。]{0,12}(違い|特徴|ポイント)です',s): flags.append('POINT')
            if flags: out.append(f"{f[5:-3]}|{','.join(flags)}|{s.strip()}")
print(len(out))
open(f'/dev/stdout','w').write('\n'.join(out))
