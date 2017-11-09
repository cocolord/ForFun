# encoding:utf-8
import os
import re
import requests
from bs4 import BeautifulSoup

#soup会打乱格式,而hacg本身格式就不标准;
#soup = BeautifulSoup(req.text,'html.parser')

#本地测试
#source = open('/home/dong/Desktop/hacg.html','r')
#soup = BeautifulSoup(source,'html.parser')
#text = soup.text

file = '/home/dong/Documents/comics.txt'
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

def getPageLink():
    # 通过改变page,可以抓取很多页;
    for i in range(28,54):
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
            }
            page = 'http://hacg.cool/wp/category/all/comic/page/'+str(i)
            req = requests.get(page, headers=headers)
            text = req.text
            pat0 = '<h1 class="entry-title"><a href=".*" rel="bookmark">.*</a></h1>'#找到页面中文章出现的那一行
            pat1 = '\"http:.*\/\"'#扣文章地址
            pat2 = 'k\"\>.*</a></h1>'#扣标题
            # test = '<h1 class="entry-title"><a href="http://hacg.cool/wp/all/game/%e5%a6%b9%e3%81%b1%e3%82%89%e3%81%a0%e3%81%84%e3%81%99%ef%bc%81%ef%bd%9e%e3%81%8a%e5%85%84%e3%81%a1%e3%82%83%e3%82%93%e3%81%a85%e4%ba%ba%e3%81%ae%e5%a6%b9%e3%81%ae%e3%82%a8%e3%83%83%e3%83%81%e3%81%97/" rel="bookmark">妹ぱらだいす！～お兄ちゃんと5人の妹のエッチしまくりな毎日～</a></h1>'
            # pat2 = '/>.*$'
            links = re.findall(pat0,text,flags=re.MULTILINE)
            #print(links)
            # 匹配网址URL的正则表达式：[a-zA-z]+://[^s]*
            #未测试
            #pat = '[a-zA-z]+://[^s]*'
            #re.findall 只能接受string字符
            for item in links:
                title = re.findall(pat2,item)
                title = ''.join(list(title))
                print(title)
                title = title.replace('</a></h1>', '')
                title = title.replace('k">', '')
                dest.writelines(title)
                item = ''.join(list(item))
                item = re.findall(pat1,item,flags=re.MULTILINE)
                item = ''.join(list(item))
                #为了清除一些特殊的格式
                item = re.sub('\n','',item)
                print(item)

                dest.writelines(item)
        except:
            print('error occurs at page '+str(i))
    dest.close()

getPageLink()


# reference:

# 多行模式
# http://www.lfhacks.com/tech/python-re-single-multiline

# BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# re 基础
# http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

# 网络请求
# http://www.jianshu.com/p/46287bd8559b

# re 网络
# http://www.jb51.net/article/73348.htm
