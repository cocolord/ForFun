# encoding:utf-8
import os
import re
import requests
from bs4 import BeautifulSoup

file = '/home/dong/Documents/hlink.txt'
req = requests.get('http://hacg.cool/wp/all/anime/少女映画nonsummerjack-nonmy-god-anubis/')
soup = BeautifulSoup(req.text,'html.parser')

fl = open(file,'a')
pat0 = '^.+'#head
pat1 = '^[\w]+' # 第一串
pat2 = '[\w]+$'#第二串
text = soup.pre.string
# text = '''[nonsummerjack (non)]My GOD ANUBIS
# 1429BA2564E7DDA16 本站不提供下载 655FBA026AE13D629A7AA93'''
# 后续可以更新匹配模式
# text = re.findall(pat,soup.pre.string,flags=re.MULTILINE)

text0 = re.findall(pat0,text)
text1 = re.findall(pat1,text,flags=re.MULTILINE)
text2 = re.findall(pat2,text)
fl.writelines(''.join((list(text0)))+'\n')
fl.writelines(('magnet:?xt=urn:btih:'+(''.join(list(text1))+''.join(list(text2))))+'\n')
fl.close()


# reference:

# 多行模式
# http://www.lfhacks.com/tech/python-re-single-multiline

# BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# re 基础
# http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

# 网络请求
# http://www.jianshu.com/p/46287bd8559b