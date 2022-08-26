
import sys

config = "modules/.files/config"

def analyze():
    if len(sys.argv) == 4:
        variable = sys.argv[2]
        value = sys.argv[3]
        print(variable.upper() + " => " + str(value))
        with open(config , "a+") as f:
            f.write(f"{variable}={value}\n")
            pass


    else:
        print("[!] Missing parameter!")
        pass

analyze()

