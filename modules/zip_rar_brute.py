import time
import zipfile

import rarfile

# requires file path , wordlist

def main(file , wordlist):
    if file.endswith(".zip"):
        file = zipfile.ZipFile(file)

    elif file.endswith(".rar"):
        file = rarfile.RarFile(file)

    else:
        print("[x] Format not supported")

    passwords = [x.strip("\n") for x in open(wordlist , "r" , errors='ignore').readlines()]

    for password in passwords:
        try:
            print(f"[>] Trying password {password}", end='\r')
            time.sleep(0.01)
            file.extractall(pwd=password.encode())
            print(f"\n[+] Password Found => {password}")
            file.close()
            break
        except:
            continue

if __name__ == '__main__':
    main(file, wordlist)






