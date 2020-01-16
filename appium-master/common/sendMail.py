#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入smtplib，MIMEText，MIMEMultipart，MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# 要发给谁
mailto_list = ["498180536@qq.com"]

# 设置服务器，用户名、口令以及邮箱的后缀
mail_host = "smtp.qq.com"
mail_user = "1928540059"
user = "1928540059@qq.com"
password = "sopkvkqnqmsadhhf"
mail_postfix = "qq.com"

# 发送邮件  
def send_mail(sub,content):
  me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
  msg = MIMEMultipart()
  msg['Subject'] = sub 
  msg['From'] = me 
  msg['To'] = ";".join(mailto_list)

  # 这是文字部分 
  part = MIMEText(content)  
  msg.attach(part) 

  # 这是附件部分    
  part = MIMEApplication(open(PATH('../report/TestResult.html'),'rb').read())  
  part.add_header('Content-Disposition', 'attachment', filename="TestResult.html")  
  msg.attach(part)

  try: 
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(user,password)
    s.sendmail(me, mailto_list, msg.as_string())
    s.close()
    return True
  except Exception as e:
    return False, str(e)