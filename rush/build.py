# Rebuilds index.html: embeds assets/*.webp into src/template.html (replaces __IMGS__).
import json,base64
m=json.load(open('src/images.json'));out={}
for k,v in m.items():
    out[k]={'src':'data:image/webp;base64,'+base64.b64encode(open(v['file'],'rb').read()).decode(),'w':v['w'],'h':v['h']}
open('index.html','w').write(open('src/template.html').read().replace('__IMGS__',json.dumps(out)))
print('index.html built')
