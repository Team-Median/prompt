from clint.textui import colored
from colorama import Fore, Back, Style

print(Fore.RED + "Adding installation modification modifiers")
print(Back.BLACK + "Reticulating splines...")
print(Style.BRIGHT + "Rendering spiders...")
print(Style.RESET_ALL)
print("Please wait...")
from pyfiglet import Figlet


def welcome(text):
    result = Figlet(font="slant")
    return colored.white(result.renderText(text))
