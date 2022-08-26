from colorama import Fore, Back


def text_color(color):
    color = color.lower()
    colors = {"red": Fore.RED,
              "white": Fore.LIGHTWHITE_EX
        , "green": Fore.GREEN
        , "magenta": Fore.LIGHTMAGENTA_EX
        , "cyan": Fore.CYAN
        , "yellow": Fore.YELLOW,
              "blue": Fore.BLUE
        , "grey": Fore.LIGHTBLACK_EX
              }

    if color in colors.keys():
        return colors.get(color)

    else:
        return Fore.CYAN


def bg_color(color):
    color = color.lower()
    colors = {"red": Back.RED,
              "white": Back.LIGHTWHITE_EX
        , "green": Back.GREEN
        , "magenta": Back.LIGHTMAGENTA_EX
        , "cyan": Back.CYAN
        , "yellow": Back.YELLOW,
              "blue": Back.BLUE
        , "grey": Back.LIGHTBLACK_EX,
              "reset": Back.RESET}

    if color in colors.keys():
        return colors.get(color)

    else:
        return Back.RED
