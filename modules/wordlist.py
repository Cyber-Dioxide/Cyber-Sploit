import random
import sys

from colorama import Fore, Style

all_col = [Style.BRIGHT + Fore.RED, Style.BRIGHT + Fore.CYAN, Style.BRIGHT + Fore.LIGHTCYAN_EX,
           Style.BRIGHT + Fore.LIGHTBLUE_EX, Style.BRIGHT + Fore.LIGHTCYAN_EX, Style.BRIGHT + Fore.LIGHTMAGENTA_EX,
           Style.BRIGHT + Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)


def exit():
    sys.exit()


def program():
    id = input(ran + "[-] Enter the name of victim: ")
    amount = input(ran + "[-] Enter the amount of passwords:")
    amount = int(amount)
    comf = input(ran + "[-] Do you want to add more information? [y/n]: ")
    file_name = input(ran+ "[*] Enter filename to save passwords: ")
    if comf == "y":
        p_num = input(ran + "[*] Enter any specific short number: ")
        ig = input(ran + "[*] Enter id name: ")
        dob = input(ran + "[*] Enter Date of birth or month name: ")
        company = input(ran + "[*] Enter comapany name: ")
        city = input(ran + "[*] Enter city name: ")
        country = input(ran + "[*] Enter Country: ")
        any = input(ran + "[*] Enter Any specific piece of information: ")

        print(ran + "\n\t\tWait it might take some seconds- - - - - -")
        file = open(f"/home/{file_name}", "a+")
        file.write(id + id + "\n")
        file.write(dob + id + "\n")
        file.write(id + p_num + "\n")
        file.write(id + company + "\n")
        file.write(id + any + "\n")
        file.write(id + city + "\n")
        file.write(city + dob + "\n")
        file.write(city + p_num + "\n")
        file.write(any + city + "\n")
        file.write(dob + country + "\n")
        file.write(dob + any + "\n")
        file.write(ig + any + "\n")
        file.write(ig + "\n")
        file.write(dob + "\n")
        for i in range(amount):
            r_num = random.randint(0000, 99999)
            r_num = str(r_num)

            file.write(id + r_num + "\n")
            file.write(p_num + r_num + "\n")
            file.write(ig + r_num + "\n")
            file.write(dob + r_num + "\n")
            file.write(company + r_num + "\n")
            file.write(city + r_num + "\n")
            file.write(country + r_num + "\n")
            file.write(any + r_num + "\n")

            file.write(r_num + any + "\n")
            file.write(r_num + id + "\n")
            file.write(r_num + p_num + "\n")
            file.write(r_num + ig)
            file.write(r_num + dob + "\n")
            file.write(r_num + company + "\n")
            file.write(r_num + city + "\n")
            file.write(r_num + country + "\n")
            file.write(r_num + r_num + "\n")

            file.write(r_num + any + "\n")
        file.close()
        print(ran + f"\nSaved in '/home/{file_name}")


    else:

        print(ran + "\t\tWait it might take some seconds... ")
        file = open(f"/home/{file_name}", "a+")
        file.write(id + id + "\n")
        for i in range(amount):
            r_num = random.randint(1000, 9999)
            r_num = str(r_num)
            file = open(f"~/{file_name}" "a+")
            file.write(id + r_num + "\n")
            file.write(r_num + r_num + "\n")

            file.write(r_num + id + "\n")
        file.close()
        print(ran + f"\n[+] Saved at /home/{file_name}")


cont = " "
while cont != "n" and "no":
        program()
