import os
import platform
import time

def rootCHEK():
    s = os.popen("whoami").read()
    if ("root") in s:
        pass
    else:
        if "aarch64" in platform.machine():
            print("Run this tool as root in Termux.")
            exit()
        elif "Linux" in platform.platform():
            print("Root your terminal for efficient performance.")
            exit(0)
        elif "Windows" in platform.platform():
            print("[!] This should be a victim  machine, not an attacker")
            exit(0)

        else:
            os.system("sudo su")

        time.sleep(3)


