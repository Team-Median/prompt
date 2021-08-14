from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


driver = webdriver.Chrome() #define Chromedriver

def open_website(url): #opens website of given url
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
        print(link)
    return link_list

def flocker_site_search(website, search_string):
    '''
    Main function so search site through search bar and return links
    '''
    open_website(website)
    time.sleep(1)
    search_main_search_bar("//*[@id='HeaderSearch_search_query']", search_string)
    results = driver.find_elements_by_class_name('product-container')
    item_list = capture_results_into_list_of_5(results)
    chosen_list = get_users_choice_of_items(item_list)
    send_user_requested_links("//*[@id='main']/div/div[2]/div/section/div/div[2]/ul/li[3]/div/a", chosen_list)
    #driver.quit()

def check_item_from_flocker_link(flocker_link):
    '''
    Function to check a specific link on footlocker.com for availability
    '''
    open_website(flocker_link)
    time.sleep(1)
    button = driver.find_element_by_class_name("Button")

    if button.text == "ADD TO CART":
        print(f"Your item is available at - {flocker_link}")
    else:
        print("still out of stock")
        driver.quit()


if __name__ == "__main__":
    flocker_site_search("http://www.footlocker.com/", "Jordan Flight Club '91")

    #check_item_from_flocker_link("https://www.footlocker.com/product/jordan-aj-1-low-boys-grade-school/53560605.html")