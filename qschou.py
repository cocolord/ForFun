import requests
import json

s = requests.session()
r = s.get('https://gateway.qschou.com/v3.0.0/index/homepage')
res = json.dumps(r.json(),indent=4)
res = res.encode('latin-1').decode('unicode_escape')
print(res)
with open('data.json','w') as f:
    json.dump(res,f)