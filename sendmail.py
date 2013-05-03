#!/usr/bin/python
import smtplib,os,sys,glob,string,re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = "nik@gmail.com"
password = "pass"

sender = "Maksimka <pingnix@gmail.com>"
to = "dnk_x_max@mail.ru"

msg = MIMEMultipart('alternative')
msg['Subject'] = "SUB"
msg['From'] = sender
msg['To'] = to

html = """ <h1 style='color: red;'> The server is down </h1> """
htmltoat = MIMEText(html,'html')
msg.attach(htmltoat)


sm=smtplib.SMTP('smtp.gmail.com','587')
sm.starttls()
sm.login(username,password)
sm.sendmail(sender, to, msg.as_string())
sm.quit()
