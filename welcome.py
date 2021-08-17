from clint.textui import colored
from colorama import Fore, Back, Style
from pyfiglet import Figlet


def welcome(text):
    result = Figlet(font='slant')
    return colored.cyan(result.renderText(text))
  
