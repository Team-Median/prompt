from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.footlocker.com/') # Opens Browser to main site
time.sleep(1) # 1 second pause
search_box = driver.find_element_by_xpath("//*[@id='HeaderSearch_search_query']") # finds the search box
search_box.send_keys("Jordan Flight Club '91")# enters selected item into search box
time.sleep(1) # 1 second pause
search_box.send_keys(Keys.ENTER)# Presses the "Enter" key to start search. most websites can use submit function below
#driver.quit()

time.sleep(3)

results = driver.find_elements_by_class_name('product-container') # grabs every search result shown on page

shoe_list = []# creating list to hold and manipulate results
for result in results:
    shoe_list.append(result)# append results to list

shoe_list = shoe_list[:5] # shortens list to first 5

link_list = []
for shoe in shoe_list:
    link = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div/section/div/div[2]/ul/li[3]/div/a").get_attribute('href')
    link_list.append(link)

for link in link_list:
    print(link)

#driver.quit()