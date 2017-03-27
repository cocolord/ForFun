# -*- coding: utf-8 -*-
import time
from email import encoders
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

_user = "he@163.com"
_pwd = "&&"
_to = "elder@163.com"

msg = MIMEMultipart()
msg['Subject'] = u'你好'.encode('gbk')
msg['From'] = u'麦克雷'.encode('gbk')
msg['To'] = _to
#attach some content
msg.attach(MIMEText('test'))

# add file:
with open('/home/maxtod/Documents/QQ.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='test.png')
    # mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    # mime.add_header('Content-ID', '<0>')
    # mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

s = smtplib.SMTP("smtp.163.com",timeout=300)
s.starttls()

s.login(_user, _pwd)  #login
for i in range(1,100):
    s.sendmail(_user,_to,msg.as_string())
    print i
    time.sleep(10)
s.close()
