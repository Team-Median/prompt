from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import threading

driver = webdriver.Chrome()

def open_website(url):
    driver.get(url)

def search_main_search_bar(xpath, search_string):
    '''
    opens the search bar and searches for given string
    '''
    search_box = driver.find_element_by_xpath(xpath)
    search_box.send_keys(search_string)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

def capture_results_into_list_of_5(results):
    '''
    grabs search results and puts the first 5 available into a list
    '''
    item_list = []
    for result in results:
        item_list.append(result)
    item_list = item_list[:5]
    return item_list

def get_users_choice_of_items(original_list):
    '''
    Shows list of results to user and grabs only the items that the user selects
    '''
    for idx, shoe in enumerate(original_list):# prints the top 5 links along with corresponding number
        print(f"{idx} - {shoe.text}") 
    print("Please type the corresponding number of the item you would like")
    user_input = input(">")
    chosen_indexes = [int(i) for i in str(user_input)]#turn suser input into list of chosen numbers
    chosen_list = [original_list[i] for i in chosen_indexes]# creates a list of only the chosen items
    return chosen_list

def send_user_requested_links(xpath, list_of_items):
    '''
    grabs the link to every item selected by user and displays in terminal
    '''
    link_list = []
    for item in list_of_items:
        link = driver.find_element_by_xpath(xpath).get_attribute('href')
        link_list.append(link)
    for link in link_list:
        print(f'Link : {link}')
    return link_list

def ebay_site_search(website, search_string):
    '''
    Main function so search site through search bar and return links
    '''
    open_website(website)
    time.sleep(1)
    search_main_search_bar('//*[@id="gh-ac"]', search_string)
    results = driver.find_elements_by_class_name('s-item')
    item_list = capture_results_into_list_of_5(results)
    chosen_list = get_users_choice_of_items(item_list)
    send_user_requested_links("//*[@id='srp-river-results']/ul/li[1]/div/div[2]/a", chosen_list)
    #driver.quit()

def check_item_from_ebay_link(ebay_link):
    '''
    Function to check a specific link on footlocker.com for availability
    '''
    open_website(ebay_link)
    time.sleep(1)
    button = driver.find_element_by_class_name("Button")

    if button.text == "ADD TO CART":
        print(f"Your item is available at - {ebay_link}")
    else:
        print("still out of stock")
        driver.quit()

# driver.get('https://ebay.com/')
# time.sleep(1) # 1 second pause

# search_box = driver.find_element_by_xpath('//*[@id="gh-ac"]') # finds the search box
# search_box.send_keys('Nike Air Jordan 1 Mid GS White Gym Red Black')# enters item into search box

# time.sleep(1) # 1 second pause

# search_box.send_keys(Keys.ENTER)# Presses the "Enter" key to start search. most websites can use submit function below

# results = driver.find_elements_by_class_name('s-item') # grabs every search result shown on page

# result_list = []# creating list to hold and manipulate results
# for result in results:
#     result_list.append(result)# append results to list

# result_list = result_list[:5]#shortening results list to only the first 5

# for idx, result in enumerate(result_list):# prints the top 5 links along with corresponding number
#     print(f"{idx} - {result.text}")

# print("Please type the corresponding number of the item you would like")
# user_input = input(">")

# chosen_indexes = [int(i) for i in str(user_input)]#turn suser input into list of chosen numbers
# chosen_list = [result_list[i] for i in chosen_indexes]# creates a list of only the items the user chose


# link_list = []
# for result in chosen_list:
#     link = driver.find_element_by_xpath("//*[@id='srp-river-results']/ul/li[1]/div/div[2]/a").get_attribute('href')
#     link_list.append(link)

# for link in link_list:
#   print(link) #ebay links are veeeeery long

# #driver.quit()
