import re,glob,sys
pat=re.compile(sys.argv[1])
for f in sorted(glob.glob('docs/[01]*/*/[0-9]*.md')):
    for i,l in enumerate(open(f).read().split('\n')):
        if '<!--' in l: continue
        t=re.sub(r'\$[^$]*\$','X',l)
        for m in pat.finditer(t):
            s=max(0,m.start()-50); print(f[5:-3],i+1,'|',t[s:m.end()+25])
