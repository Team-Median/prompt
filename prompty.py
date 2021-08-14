from io import StringIO
from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import re, click, urllib, json, time, requests

browser = webdriver.Chrome

f = Figlet(font="slant")
print(f.renderText(">  prompt"))

print(
    """> Welcome! We help you by checking availability of your items at the following stores:
[BBY]Best Buy, [NWE]Newegg, [FOT]Footlocker, [FCL]FlightClub, [EBY]Ebay

> 1. Search for the item at one of the stores listed above.
  2. Copy the URL from that search.
  3. At the prompt, type the [store code], [search result URL for your item] and press [Enter]

> <Coming Soon> [store code], [Search Result URL] <Enter>

> <For Now> We took your keyword and applied that to the search on YouTube. Enjoy Searching…!
"""
)
