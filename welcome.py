from clint.textui import colored
from colorama import Fare, Back, Style
from pyfiglet import pyfiglet


def welcome(text):
    result = Figlet(font='slant')
    return colored.cyan(result.renderText(text))
  