#encoding: utf-8
import re
import pandas as pd
import requests
import codecs
import sys
import traceback
from snownlp import SnowNLP
from os import path
import snownlp
ret = set()
neg = codecs.open('negative_comments.txt','w')
with codecs.open('iphonexcomments.txt','w') as ip:
    for i in range(1,100):
        try:
            response = requests.get(
                'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2007&productId=5089235&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1')
            response = response.text.encode('utf-8')
            pat = '"content":"(.*?)",'
            res = re.findall(pat, response)
            for j in res:
                j = j.replace('\\n','')
                j1 = SnowNLP(j)
                ret.add(j)
                if j1.sentiments < 0.05:
                    neg.write(j)
                    neg.write('\n')
        except:
		    traceback.print_exc()
    for i in ret:
        ip.write(i+'\n')