import re
import pandas as pd
import requests
from os import path
with open('iphonexcomments.txt','wt') as ip:
    for i in range(1,120):
        try:
            response = requests.get(
                'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2007&productId=5089235&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1')
            response = response.text
            pat = '"content":"(.*?)",'
            res = re.findall(pat, response)
            for j in res:
                j = j.replace('\\n','')
                if i%2==0:
                    ip.write(j)
                    ip.write('\n')
        except:
            print('爬第'+str(i)+'出现问题')
            continue
