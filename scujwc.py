#coding=utf-8
import urllib
import urllib2
import cookielib
import requests
import HTMLParser
from bs4 import BeautifulSoup
import re
class JWC:
    def __init__(self):
        self.loginURL = 'http://202.115.47.141/loginAction.do'
        self.crawlURL = 'http://202.115.47.141/bxqcjcxAction.do'
        self.cookiename = 'cookie.txt'
        self.cookie = cookielib.MozillaCookieJar(self.cookiename)
        self.handler = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.handler)
        self.postdata = urllib.urlencode({
            'zjh': "2015141052004",
            'mm': "2881856"
        })
        self.agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        self.headers = {'User-Agent ':self.agent}
        self.html_parser = HTMLParser.HTMLParser()
        self.allGrades = []

    def getPage(self):
        request = self.opener.open(self.loginURL,self.postdata)
        self.cookie.save(ignore_discard=True, ignore_expires=True)
        request = self.opener.open(self.crawlURL)
        sourceCode = request.read().decode('gbk')
        return sourceCode

    def parsePage(self):

        sourceCode = self.getPage()
        if not sourceCode:
            raise 'Page Read Error'
        pattern = re.compile(
            r'<tr class="odd".*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</td>',
            re.S)
        items = re.findall(pattern, sourceCode)
        print items
        #pattern = '<td align="center"> .*? </td>'
        #items = re.findall(pattern,sourceCode,flags = re.MULTILINE)
        grades = []
        for item in items:
            grades.append(
                [item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip(), item[4].strip(), item[5].strip(),
                 item[6].strip()])
            # grades.append([self.html_parser.unescape(item[0].strip()),self.html_parser.unescape(item[1].strip())])
        print grades
        return grades

    def printGrades(self):
        self.allGrades = self.parsePage()
        index = 1
        for item in self.allGrades:
            print u'课程号:%s\t 课序号:%s\t 课程名:%s\t 英文课程名:%s\t 学分:%s\t 课程属性:%s\t 成绩:%s\t\n' % (
            item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            index += 1

if __name__ == '__main__':
    jwc = JWC()
    jwc.printGrades()
