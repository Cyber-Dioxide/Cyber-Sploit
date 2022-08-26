import socket
host = input("[+] Enter url (google.com): ")
def find(host):

    ip = socket.gethostbyname(host)
    print("The ip is :")
    print(("[" + ip + "]"))

find(host)
