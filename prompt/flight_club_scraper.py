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
    '''opens website of given url'''
    driver.get(url)

def search_main_search_bar(el_id, search_string):
    '''opens the search bar and searches for given string'''
    search_box = driver.find_element_by_id(el_id)
    search_box.send_keys(search_string)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

def capture_results_into_list_of_5(results):
    '''grabs search results and puts the first 5 available into a list'''
    item_list = []
    for result in results:
        item_list.append(result)
    
    original_list = item_list[:5]
    return original_list

def create_index_list(user_input):
    '''turn user input into list of chosen numbers'''
    chosen_indexes = [int(i) for i in str(user_input)]
    return chosen_indexes

def create_chosen_list(original_list, chosen_indexes):
    '''creates a list of only the chosen items'''
    chosen_list = [original_list[i] for i in chosen_indexes]
    return chosen_list


def get_users_choice_of_items(original_list):
    '''
    Shows list of results to user and grabs only the items that the user selects
    '''
    for idx, shoe in enumerate(original_list):
        print(f"{idx} - {shoe.text}")

    print("Please type the corresponding number of the item you would like")
    user_input = input(">")
    chosen_indexes = create_index_list(user_input)
    chosen_list = create_chosen_list(original_list, chosen_indexes)
    return chosen_list

def send_user_requested_links(xpath, list_of_items):
    '''
    grabs the link to every item selected by user and displays in terminal
    '''
    link_list = [elem.get_attribute('href') for elem in list_of_items]

    for link in link_list:
        print(f'Link : {link}')
    return link_list

def fc_site_search(website, search_string):
    '''
    Main function so search site through search bar and return links
    '''
    open_website(website)
    time.sleep(1)
    search_main_search_bar("NavigationSearchInput", search_string)
    results = driver.find_elements_by_class_name('sc-1wc5x2x-0')
    item_list = capture_results_into_list_of_5(results)
    chosen_list = get_users_choice_of_items(item_list)
    send_user_requested_links("//*[@id='main']/div/div[2]/div/section/div/div[2]/ul/li[3]/div/a", chosen_list)

def display_out_of_stock():
    print("display_out_of_stock")





def check_item_from_fc_link(fc_link):
    '''takes in a link and searches to see if item is available'''
    open_website(fc_link) 
    time.sleep(1) # 1 second pause
    button1 = driver.find_element_by_class_name("sc-1t2dcr4-0")

    if button1.text == "OUT OF STOCK":
        display_out_of_stock()
        time.sleep(5)
        check_item_from_fc_link(fc_link)
    else:
        print(f"Your item is available at - {fc_link}")
        open_website(fc_link)
       
        time.sleep(3)
        button2 = driver.find_element_by_class_name("sc-1t2dcr4-0")
        button2.click()
        time.sleep(3)
        
        buttons_list = driver.find_elements_by_tag_name("button")

        for button in buttons_list:
            if button.text == "CHECK OUT":
                button.click()
                return
        
        time.sleep(3)

if __name__ == "__main__":

    fc_site_search('http://www.flightclub.com/', "AIR JORDAN 1 HIGH RETRO")
    
