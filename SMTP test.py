# -*- coding: utf-8 -*-
import time
import smtplib
from email import*
from email.mime.text import MIMEText

_user = "any@163.com"
_pwd = "**"
_to = "who@163.com"
msg = MIMEText('','html')#content here
msg['Subject'] = u'你好'.encode('gbk')
msg['From'] = u'麦克雷'.encode('gbk')
msg['To'] = _to

s = smtplib.SMTP("smtp.163.com",timeout=300)
s.starttls()

s.login(_user, _pwd)  #login
for i in range(1,100):
    s.sendmail(_user,_to,msg.as_string())
    print i
    time.sleep(10)
s.close()
