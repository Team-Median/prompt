from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import bs4

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.flightclub.com/') # Opens Browser to main site
time.sleep(1) # 1 second pause
search_box = driver.find_element_by_id('NavigationSearchInput') # finds the search box
search_box.send_keys('NIKE LEBRON 8 V/2 LOW “SOLAR RED”')# enters selected item into search box
time.sleep(1) # 1 second pause
search_box.send_keys(Keys.ENTER)# Presses the "Enter" key to start search. most websites can use submit function below
time.sleep(1) # 1 second pause. give time for results to return

results = driver.find_elements_by_class_name('sc-1wc5x2x-0') # grabs every search result shown on page

shoe_list = []# creating list to hold and manipulate results
for result in results:
    shoe_list.append(result)# append results to list

shoe_list = shoe_list[:5]#shorten results list to first 5

for shoe in list(shoe_list):# must make a copy of list before iterating and removing
    if '$' not in shoe.text:# iterate through list of results and remove items not in stock
        shoe_list.remove(shoe)

links = [elem.get_attribute('href') for elem in shoe_list]# list comprehension to grab the links to each available item in the results list

for link in links:
  print(link)