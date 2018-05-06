# encoding:utf-8
#
import re
cls = '						<h1 class="entry-title"><a href="http://hacg.cool/wp/all/comic/c92-%e9%bb%92%e3%83%9f%e3%82%b5%e4%bc%9a%e5%a0%b4-%e6%b1%a0%e5%92%b2%e3%83%9f%e3%82%b5-%e4%ba%ba%e5%bd%a2%e9%81%8a%e6%88%af-nierautomata/" rel="bookmark">(C92) [黒ミサ会場 (池咲ミサ)] 人形遊戯 (NieRAutomata)</a></h1>'

pat0 = '<h1 class="entry-title"><a href=".*" rel="bookmark">.*</a></h1>'
#可能存在几种格式
pat = '\"http:.*\/\"'
pat1 = '\"http:.*\n.*\/\"'
links = re.findall(pat0,cls,flags=re.MULTILINE)
print(links)
links2string = ''.join(list(links))
links2string = re.findall(pat,links2string)
links2string = ''.join(list(links2string))
links2string = re.sub('\n','',links2string)
print(links2string)