import ipapi
from colorama import Fore

c = Fore.CYAN
r = Fore.LIGHTRED_EX


def program(ip):
    location = ipapi.location(ip)

    for k, v in location.items():
        print(c + k + " : " + r + str(v))


yes = ['y', 'yes']
no = ['n', 'no']

cont = ""

try:
    program(ip)
except:
    print(f"{c}[{r}!{c}] {r}Something went wrong")
    cont = input(c + "Do you want to continue? [y/n]")
