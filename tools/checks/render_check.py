import subprocess,glob,re,os,sys
from concurrent.futures import ThreadPoolExecutor
CH=os.environ.get("CHROME","/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
pages=sorted(glob.glob(sys.argv[1]+'/'+(sys.argv[2] if len(sys.argv)>2 else '06solid_state')+'/*/*/index.html'))
def run(p):
    rel=p.split('/site/')[1].replace('index.html','')
    url='http://localhost:8765/'+rel
    out=subprocess.run([CH,'--headless=new','--no-sandbox','--disable-gpu','--virtual-time-budget=10000','--dump-dom',url],capture_output=True,text=True,timeout=90).stdout
    err=out.count('<mjx-merror'); cont=out.count('<mjx-container')
    src=open(p).read(); ar=src.count('class="arithmatex"')
    return rel,err,cont,ar
with ThreadPoolExecutor(6) as ex:
    res=list(ex.map(run,pages))
bad=[r for r in res if r[1] or r[2]<r[3]]
print(len(res),'pages; problems:',bad)
