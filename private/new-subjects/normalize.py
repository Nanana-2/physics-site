"""生成された md の機械的な整形（Claude 用）。 python3 normalize.py files...
- 各小問の解説の冒頭にある手順の宣言文（「〜を利用します。」など1文だけの段落）を消す
- $$ の前後に空行を入れる
- 微分の d を \mathrm{d} にする（\frac{d..}{d..}，\, dx など）
"""
import re,sys
NARR_OLD=re.compile(r'^[^。\n$]{0,60}(?:\$[^$\n]*\$[^。\n$]{0,40})*(を利用します|を計算します|を求めます|を適用します|を導きます|を用います|を確認します|を考えます|に着目します|を代入します|を立てて[^。]*|を示します|を行います|を整理します|を比較します|を調べます|を解きます|を使います)。$')
NARR=re.compile(r'^[^。\n$]{4,70}します。$')
def norm(t):
    # 1) narration first paragraph of each ### section
    def sec(m):
        head,body=m.group(1),m.group(2)
        paras=body.split('\n\n',1)
        first=paras[0].strip()
        if len(paras)>1 and NARR.match(first) and '$' not in first:
            body=paras[1]
        return head+body
    t=re.sub(r'(^### \(\d\)\n)(.*?)(?=^### |\Z)',sec,t,flags=re.S|re.M)
    # 2) blank lines around $$ blocks
    out=[];lines=t.split('\n');inblk=False
    for i,l in enumerate(lines):
        if l.strip()=='$$':
            if not inblk and out and out[-1].strip()!='': out.append('')
            out.append(l); inblk=not inblk
            if not inblk and i+1<len(lines) and lines[i+1].strip()!='': out.append('')
        else: out.append(l)
    t='\n'.join(out)
    # 3) differentials
    t=re.sub(r'\\frac\{d\}\{d([a-zA-Z])\}',r'\\frac{\\mathrm{d}}{\\mathrm{d}\1}',t)
    t=re.sub(r'\\frac\{d\^\{?(\d)\}?\}\{d([a-zA-Z])\^\{?\1\}?\}',r'\\frac{\\mathrm{d}^\1}{\\mathrm{d}\2^\1}',t)
    t=re.sub(r'\\frac\{d\^\{?(\d)\}? ?([a-zA-Z](?:_[a-zA-Z0-9{}]+)?)\}\{d([a-zA-Z])\^\{?\1\}?\}',r'\\frac{\\mathrm{d}^\1\2}{\\mathrm{d}\3^\1}',t)
    t=re.sub(r'\\frac\{d ?([a-zA-Z\\][a-zA-Z{}_^0-9\\]*?)\}\{d([a-zA-Z])\}',r'\\frac{\\mathrm{d}\1}{\\mathrm{d}\2}',t)
    t=re.sub(r'(\\,|\;|\s)d([xyztsuvrkθωφ]|\\theta|\\phi|\\varphi|\\omega|\\tau|\\xi|\\lambda|\\boldsymbol\{[A-Za-z]\}|[VSl])(?![a-zA-Z])',r'\1\\mathrm{d}\2',t)
    t=re.sub(r'(?<![a-zA-Z\\])d([A-Za-z](?:_\{?[A-Za-z0-9\\]+\}?)?)?/d([a-z])(?![a-zA-Z])',lambda m:'\\mathrm{d}'+(m.group(1) or '')+'/\\mathrm{d}'+m.group(2),t)
    t=re.sub(r'\\mathrm\{d\}\s+\\mathrm\{d\}',r'\\mathrm{d}',t)
    return t
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read(); n=norm(s)
    if n!=s: open(f,'w',encoding='utf-8').write(n)
