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
    '''opens the search bar and searches for given string'''
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
    for idx, shoe in enumerate(original_list):# prints the top 5 links along with corresponding number
        print(f"{idx} - {shoe.text}") 
    print("Please type the corresponding number of the item you would like")
    user_input = input(">")
    chosen_indexes = create_index_list(user_input)#turn suser input into list of chosen numbers
    chosen_list = create_chosen_list(original_list, chosen_indexes)# creates a list of only the chosen items
    return chosen_list

def send_user_requested_links(xpath, list_of_items):
    '''
    grabs the link to every item selected by user and displays in terminal
    '''
    link_list = []
    for item in list_of_items:
        link = driver.find_element_by_xpath(xpath).get_attribute('href')
        link_list.append(link)
    #print(link_list)
    for link in link_list:
        print(f'Link : {link}')
    # return link_list

def newegg_site_search(website, search_string):
    '''
    Main function so search site through search bar and return links
    '''
    open_website(website)
    time.sleep(1)
    search_main_search_bar('//*[@id="app"]/header/div[1]/div[3]/div[1]/form/div/div[1]/input', search_string)
    results = driver.find_elements_by_class_name('item-cell')# changed class name
    item_list = capture_results_into_list_of_5(results)
    chosen_list = get_users_choice_of_items(item_list)
    send_user_requested_links("//*[@id='item_cell_9SIARCJF9M7893_1_0']/div/a", chosen_list)#changed xpath

def check_item_from_newegg_link(newegg_link):
    '''
    Function to check a specific link on newegg.com for availability
    '''
    open_website(newegg_link)
    time.sleep(1)
    button = driver.find_element_by_class_name("Button")
    if button.text == "ADD TO CART":
        print(f"Your item is available at - {newegg_link}")
    else:
        print("still out of stock")
        driver.quit()
        
if __name__ == "__main__":
    
    newegg_site_search("https://www.newegg.com/", "rtx 3080")
