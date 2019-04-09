# -*- coding: utf-8 -*-
import requests
import json
import io
import socket
s = requests.session()
r = s.get('https://gateway.qschou.com/v3.0.0/index/homepage')
res = json.dumps(r.json(),indent=4)
ret = res.encode('latin-1').decode('unicode_escape')
print(ret)
with io.open('data.json','w') as f:
    json.dump(ret,f,ensure_ascii=False,indent=4)