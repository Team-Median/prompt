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
search_box.send_keys("AIR JORDAN 1 HIGH RETRO")# enters selected item into search box
time.sleep(1) # 1 second pause
search_box.send_keys(Keys.ENTER)# Presses the "Enter" key to start search. most websites can use submit function below
time.sleep(1) # 1 second pause. give time for results to return

results = driver.find_elements_by_class_name('sc-1wc5x2x-0') # grabs every search result shown on page

shoe_list = []# creating list to hold and manipulate results
for result in results:
    shoe_list.append(result)# append results to list


for shoe in list(shoe_list):# must make a copy of list before iterating and removing
    if '$' not in shoe.text:# iterate through list of results and remove items not in stock
        shoe_list.remove(shoe)
shoe_list = shoe_list[:5]#shorten results list to first 5


for idx, shoe in enumerate(shoe_list):# prints the top 5 links along with corresponding number
    print(f"{idx} - {shoe.text}")

print("Please type the corresponding number of the item you would like")
user_input = input(">")

chosen_indexes = [int(i) for i in str(user_input)]#turn suser input into list of chosen numbers
chosen_list = [shoe_list[i] for i in chosen_indexes]# creates a list of only the items the user chose


links = [elem.get_attribute('href') for elem in chosen_list]# list comprehension to grab the links to each available item in the results list

for link in links:
  print(link)

#driver.quit()


def check_item_from_fc_link(fc_link):
    driver = webdriver.Chrome()
    driver.get(fc_link)
    time.sleep(1) # 1 second pause
    button = driver.find_element_by_class_name("sc-1t2dcr4-0")

    if button.text == "OUT OF STOCK":
        print("still out of stock")
        driver.quit()
    else:
        print(f"Your item is available at - {fc_link}")

#check_item_from_fc_link("https://www.flightclub.com/air-jordan-1-high-retro-black-varsity-red-011062")