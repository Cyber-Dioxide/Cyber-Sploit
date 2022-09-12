import os
import subprocess
from files.rootCheck import rootCHEK
from files.loading import animate
from files.banner import dt, render
from files.colors import text_color
import json

W = text_color("white")
C = text_color("cyan")
Y = text_color("yellow")
R = text_color('red')
G = text_color("green")

dir = "/home/" + os.getlogin() + "/Cyber-Sploit-Output"


def cmd(command):
    os.system(command)


print(render())
animate()
# rootCHEK()

if os.path.isdir(dir):
    pass
else:
    os.mkdir(dir)

if os.path.exists("modules/.files/config"):
    os.remove("modules/.files/config")
else:
    pass


def msg(mesg, logo="!"):
    print(f"{W}[{R}{logo}{W}] {mesg}")


def set(data):
    analyze = ""
    for d in data:
        analyze += d
        analyze += " "
    cmd(f"python3 set.py {analyze}")


def show_modules():
    for line in [x.strip('\n') for x in open("modules_description", "r").readlines()]:
        msg(f"{C}{line}", logo=f"{C}*")


def use_module(module):
    modules = os.listdir("modules")
    if module in modules:
        return True
    else:
        return False


def format(type, module):
    if os.path.exists(dir + "/" + module):
        os.remove(dir + "/" + module)

    if type.lower() == "exe":
        os.mkdir("formatted_modules")
        supported_formats = ['py', 'exe', '.py', '.exe']
        if type in supported_formats:

            if type == "exe":
                cmd(f"cp modules/{module}formatted_modules")

                cmd(f"pyinstaller --onefile --noconsole formatted_modules/{module}")
                cmd(f"mv modules/dist/{module.replace('.py', '')}.exe {dir}/")
                msg(logo="*", mesg=f"{C}Access file at: {Y}~/Cyber-Sploit-Output/{module.replace('.py', '')}.exe")
                return True

            else:
                cmd(f"cp modules/{module} {dir}/")
                msg(logo="*", mesg=f"{C}Access file at: {Y}{dir}/{module}")
                return True

        else:
            return False


def database_search(module):
    file = module.replace(".py", ".json")

    c_file = f"database/{file}"

    if file in os.listdir("database"):
        with open(c_file) as DJ:
            data = json.loads(DJ.read())
        for key, value in data.items():
            if key == "Parameters":
                value = str(value)

            if type(value) == list:
                for val in value:
                    msg(f"{key}\t==>\t{val}", logo=f"{Y}*")

            else:
                msg(f"{key}\t==>\t{value}", logo=f"{C}*")

    else:
        msg(f"""Select A module to see info.
        +---------------------------------+
        |        {Y}</>  {W} Cyber-Sploit       |
        |       {Y}</>  {W}Developer: Saad-Khan |
        |       {Y}</>  {W}Author: Cyber-Dioxide|
        +---------------------------------+
        """, logo="/\\")


def check_parameters(module):
    base = f"database/{module.replace('.py', '.json')}"
    if module.replace(".py", ".json") not in os.listdir("database"):
        msg("No info found")
        msg(mesg=f'{G}This module have no requirements, Just run it', logo=f'{Y}*')
    else:
        folder = "parameters/parameters.json"
        keys = list()
        with open(base, "r") as ded:
            deb = json.loads(ded.read())
            for k, v in deb.items():
                if k == "Parameters":
                    keys = v
                    print(keys)
                else:
                    pass

        with open(folder, "r") as para:
            data = json.loads(para.read())
            for key, val in data.items():
                if key in keys:
                    msg(f"{C}{key}\t{W}=>\t{Y}{val}", logo=f"{Y}~")
                elif key not in keys:
                    continue
                else:
                    msg(mesg=f'{G}This module have no requirements, Just run it', logo=f'{Y}*')


def shell():
    module = ""
    command = ""
    while "exit" not in command:
        command = input(f"{W}[{Y}{dt()}{W}]/{C}{module}{W}-# " + W).lower()
        command = list(command.split(" "))

        if command[0] == "set":
            with open("parameters/parameters.json" ,"r") as f:
                f = f.read()
            params = json.loads(f)
            params = params.items()
            for k, v in params:
                if command[1] == k:
                    try:
                        set(command)
                    except:
                        pass

            # else:
            #     msg("Incorrect parameter" , logo="!")

        elif command[0] == "use":
            # command = command.remove("use")
            check = use_module(command[1])
            if check:
                module = command[1]

            else:
                print(f"{W}[{R}!{W}] {R}Module {W}{module} not found! ")
                module = ""

        elif "run" in command:
            cmd(f"python3 RUN.py {module}")

        elif "generate" in command:
            with open(module, "r") as gen:
                gen = gen.read()
            with open(dir + "/" + module, "a+") as rate:
                rate.write(gen)

        elif "format" in command:
            formate = command[1]
            supported_formats = ['py', 'exe', '.py', '.exe']

            if formate in supported_formats:
                format(type=formate, module=module)

            else:
                msg(f"{Y} Supported formats")
                msg(f"{Y}py", logo="*")
                msg(f"{Y} exe", logo="*")

        elif "help" in command:
            for line in [x.strip('\n') for x in open("files/.help", "r").readlines()]:
                msg(mesg=f"{Y}{line}", logo=f"{C}+")

        elif "info" in command:
            database_search(module)

        elif "show" in command:
            show_modules()
        elif command[0] == "banner":
            print(render())
        elif 'options' in command:
            try:
                check_parameters(module)
            except:
                msg(mesg=f'{G}This module have no requirements, Just run it', logo=f'{Y}*')
                pass

        elif command[0] == "back":
            module = ""

        elif command[0] == "search":
            os.system(f"ls modules/ | grep {command[1]}")
        else:
            msg(f"{C}Executing... {Y}{command}", logo=f"{G}+")
            subprocess.call(command, shell=True, stderr=True)


try:
    shell()
except:
    print("\n")
    msg(f"{R}Something went wrong... Try again")
    pass
