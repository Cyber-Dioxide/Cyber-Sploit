import marshal
import sys
from colorama import Fore


if len(sys.argv) < 2:
    print(f"{Fore.RED} You are an idiot\n {Fore.LIGHTWHITE_EX}Usage: python3 {Fore.YELLOW}Encode_my_code.py <input_file> <output_file>")
    exit()

input_file = sys.argv[1]

ouput_file = sys.argv[2]



def encode_():
    with open(input_file , "r") as f:
        f = f.read()

    comp = compile(f , "Code" , "exec")
    return marshal.dumps(comp)


def output():

    data = f"""
import marshal
exec(marshal.loads({encode_()}))
    
    """

    with open(ouput_file , "w") as d:
        d.writelines(data)

    print(Fore.LIGHTWHITE_EX , f"[+]{Fore.CYAN} Encoded successfully!")

output()
