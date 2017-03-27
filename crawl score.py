import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup
import re
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
postdata = urllib.urlencode({
    'zjh':"2015141052011",
    'mm':"xxx"
})
url = 'http://202.115.47.141/loginAction.do'
result = opener.open(url,postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
result = opener.open('http://202.115.47.141/bxqcjcxAction.do')
soup = BeautifulSoup(result,'lxml')
print soup
print(soup.find_all("tr","odd"))
#scu jwc网站真的蛋疼
