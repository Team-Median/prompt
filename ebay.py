from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import bs4

driver = webdriver.Chrome()
driver.get('https://ebay.com/')
time.sleep(1) # 1 second pause

search_box = driver.find_element_by_xpath('//*[@id="gh-ac"]') # finds the search box
search_box.send_keys('Nike Air Jordan 1 Mid GS White Gym Red Black')# enters item into search box

time.sleep(1) # 1 second pause

search_box.send_keys(Keys.ENTER)# Presses the "Enter" key to start search. most websites can use submit function below

results = driver.find_elements_by_class_name('s-item') # grabs every search result shown on page

result_list = []# creating list to hold and manipulate results
for result in results:
    result_list.append(result)# append results to list

result_list = result_list[:5]#shortening results list to only the first 5

link_list = []
for result in result_list:
    link = driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[1]/div/div[2]/a").get_attribute('href')
    link_list.append(link)

for link in link_list:
  print(link) #ebay links are veeeeery long

#driver.quit()