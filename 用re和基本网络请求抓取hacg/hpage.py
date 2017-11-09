# encoding:utf-8
import os
import re
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"

}

#通过改变page,可以抓取很多页;
page = 'http://hacg.cool/wp/category/all/comic/page/3'
req = requests.get(page,headers = headers)

#soup会打乱格式,而hacg本身格式就不标准;
#soup = BeautifulSoup(req.text,'html.parser')

#本地测试
#source = open('/home/dong/Desktop/hacg.html','r')
#soup = BeautifulSoup(source,'html.parser')
#text = soup.text

text = req.text
file = '/home/dong/Documents/hpage.txt'
dest = open(file,'a')
#dest = open(file,'w')
#测试re
# cls = '<a href="http://hacg.cool/wp/all/comic/%e4%b8%8a%e9%80%a3%e9%9b%80%e4%b8%89%e5%b9%b3-anal-angel-%e4%b8%8d%e5%86%a0%e5%90%8d%e6%b1%89%e5%8c%96/#more-6300" class="more-link">'
# pat = '<a href=".*" class="more-link">'
# cls = '<h1 class="entry-title"><a href="http://hacg.cool/wp/all/comic/%e6%bd%ae%e9%a2%a8%e3%82%b5%e3%83%b3%e3%82%b4-%e5%a6%b9%e3%81%ae%e3%81%8a%e3%81%be%e3%80%87%e3%81%93-mujin%e3%82%b3%e3%83%9f%e3%83%83%e3%82%af%e3%82%b9/" rel="bookmark">[潮風サンゴ] 妹のおま〇こ MUJINコミックス</a></h1>'
# pat = '<h1 class="entry-title"><a href=".*" rel="bookmark">.*</a></h1>'
# cls = '''						<h1 class="entry-title"><a href="http://hacg.cool/wp/all/comic/%e3%81%84%e3%83%bc%e3%82%80%e3%81%99%e3%83%bb%e3%82%a2%e3%82%ad-
# %e3%81%a8%e3%82%8d%e3%81%be%e3%82%93%e3%82%b9%e3%82%bf%e3%82%a4%e3%83%ab%e6%97%a0%e6%af%92%e6%b1%89%e5%8c%96%e7%bb%84/" rel="bookmark">[いーむす・アキ] とろまんスタイル[无毒汉化组]</a></h1>'''
# pat = '<h1 class="entry-title"><a href=".*|.*-\n.*" rel="bookmark">.*</a></h1>'


#可以扣htmlsource里的文章了!
#但是格式可能存在不同 有时可能有换行
#pat0 = '<h1 class="entry-title"><a href=".*-\n.*" rel="bookmark">.*</a></h1>'
#pat0 = '<h1 class="entry-title"><a href=".*|.*-\n.*" rel="bookmark">.*</a></h1>'


pat0 = '<h1 class="entry-title"><a href=".*" rel="bookmark">.*</a></h1>'
pat1 = '\"http:.*\/\"'
links = re.findall(pat0,text,flags=re.MULTILINE)
print(links)
#re.findall 只能接受string字符
for links2string in links:
    links2string = ''.join(list(links2string))
    links2string = re.findall(pat1,links2string,flags=re.MULTILINE)
    links2string = ''.join(list(links2string))
    #为了清除一些特殊的格式
    links2string = re.sub('\n','',links2string)
    print(links2string)
    dest.writelines(links2string)
dest.close()