import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465
context = ssl.create_default_context()

username = 'gsp672021@gmail.com'
password = 'gbiylefkztnirvyh'

receiver = 'gritsun.sp@gmail.com'

message = """\
Subject: Hello my dear friend!
How are you? """

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
