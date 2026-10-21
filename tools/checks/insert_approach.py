import sys, re, glob, importlib.util
subj, mod = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("m", mod); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
files = {f.split('/',2)[2][:-3]: f for f in glob.glob(f'docs/{subj}/*/[0-9]*.md')}
assert set(files) == set(m.A), (set(files) ^ set(m.A))
for k, txt in m.A.items():
    # lint: commas, clipped potentials, naming style
    for s in re.split(r'(?<=。)', re.sub(r'\$[^$]*\$', 'X', txt)):
        if s.count('，') >= 2: print('COMMA', k, s)
    if re.search(r'(解け|書け|扱え|使え|求められ)ます|これが.{1,12}です', txt): print('STYLE', k)
    f = files[k]; t = open(f).read()
    if 'class="approach"' in t: print('SKIP', k); continue
    new, n = re.subn(r'(## 解答・解説\n\n)(### \(1\))', r'\1<div class="approach" markdown>\n' + txt.replace('\\', '\\\\') + r'\n</div>\n\n\2', t, count=1)
    if n != 1: print('NOFIT', k); continue
    open(f, 'w').write(new)
print('ok')
