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
import threading


f = Figlet(font="slant")
print(f.renderText(">  prompt"))

print(
    """> Welcome! We help you by checking availability of your items at the following stores:
[BBY]Best Buy, [NWE]Newegg, [FOT]Footlocker, [FCL]FlightClub, [EBY]Ebay

> 1. Search for the item at one of the stores listed above.
  2. Copy the URL from that search.
  3. At the prompt, type the [store code], [search result URL for your item] and press [Enter]
  4. Don't have a link? No worries! Type the [store code], [search phrase] and press [Enter] 
"""
)
search_string = input(">")
split_search_string = search_string.split(" ")



# For FlightClub
if split_search_string[0].upper() == "FCL":
  if split_search_string[1][0:4] == "http":
    item_check_link = split_search_string[1]
    import flight_club_scraper as fcs
    t = threading.Timer(5.0, fcs.check_item_from_fc_link, args=(item_check_link,))
    t.start()
  else:
    search_phrase = split_search_string[1]
    import flight_club_scraper as fcs
    fcs.fc_site_search('http://www.flightclub.com/', search_phrase)

# > <Coming Soon> [store code], [Search Result URL] <Enter>

# > <For Now> We took your keyword and applied that to the search on YouTube. Enjoy Searching…!
# """
# )