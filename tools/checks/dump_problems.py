import re,glob,sys
for f in sorted(glob.glob(f'docs/{sys.argv[1]}/*/[0-9]*.md')):
    t=open(f).read()
    title=re.search(r'^# (.+)$',t,re.M).group(1)
    prob=t.split('## 問題',1)[1].split('\n---',1)[0]
    prob=re.sub(r'<!--.*?-->|<figure.*?</figure>','',prob,flags=re.S)
    paras=[p.strip().replace('\n',' ') for p in prob.split('\n\n') if p.strip()]
    intro=[p for p in paras if not re.match(r'\(\d\)',p)]
    subs=[p for p in paras if re.match(r'\(\d\)',p)]
    print('##',f.split('/',2)[2][:-3],title,'|',' '.join(intro)[:220])
    for s in subs: print('  ',s[:150])
