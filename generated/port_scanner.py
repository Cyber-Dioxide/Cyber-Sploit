ip="192.158.236.180"
from nmap.nmap import PortScanner#importing the nmap module

scanner = PortScanner()  #creating variable named scanner and calling the portscanner class

print("Welcome, this is a simple nmap automation tool")
print("<----------------------------------------------------->")

def scan(ip_addr):
    resp = input("""Please enter the type of scan you want to run
                    1)SYN ACK Scan
                    2)UDP Scan
                    3)Comprehensive Scan
                    4)IP protocol ping """)  # selecting the specific scan as per user response

    print("You have selected option: ", resp)

    if resp == '1':
        print("Nmap Version: ",
              scanner.nmap_version())  # calling additional functionality method using scanner variable
        scanner.scan(ip_addr, '1-1024', '-v -sS')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())  # .state for getting the status of the host
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())  # .keys retunrs all active ports within the range
    elif resp == '2':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    elif resp == '3':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    elif resp == '4':
        print("Nmap Version: ", scanner.nmap_version())
        scanner.scan(ip_addr, '1-1024', '-v -PO')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    elif resp >= '5':
        print("Please enter a valid option")

scan(ip_addr=ip)