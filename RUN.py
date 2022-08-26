import os
import sys

config_file = "modules/.files/config"

modulez = sys.argv[1]

module_path = f"modules/{modulez}"

if os.path.exists(f"generated/{modulez}"):
    os.remove(f"generated/{modulez}")


def read_config(module):
    config_values = [x.strip("\n") for x in open(config_file, "r").readlines()]

    for parameter in config_values:
        variable, value = parameter.split("=")

        parameter = variable + "=" + f"\"{value}\""

        with open(module, "r") as append:
            data = append.read()

        with open(f"generated/{modulez}", "a+") as files:
            files.write(parameter + "\n")

    with open(f"generated/{modulez}", "a+") as file:
            file.write(data)


def run():
    try:
        read_config(module_path)
        os.system(f"python3 generated/{modulez}")
    except:
        os.system(f"python3 modules/{modulez}")

    if os.path.exists("modules/.files/config"):
        os.remove("modules/.files/config")

try:
    run()
except:
    print("[+] Set parameters are removed!")
    print("[+] Something went wrong, select module again and set parameters.")
