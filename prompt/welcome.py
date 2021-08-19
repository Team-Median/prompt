from clint.textui import colored
from colorama import Fore, Back, Style

# print(Fore.RED + "some red text")
print(Back.BLACK + "and with a green background")
print(Style.BRIGHT + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")
from pyfiglet import Figlet


def welcome(text):
    result = Figlet(font="slant")
    return colored.white(result.renderText(text))
