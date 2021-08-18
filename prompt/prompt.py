from io import StringIO
import os
from pyfiglet import Figlet
import re, click, urllib, json, time, requests
from requests.models import Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import threading
import helpdoc 
from welcome import welcome


def main():
    """
    Simple CLI for querying
    """
    os.system("clear")
    print(welcome("> prompt"))
    print("Welcome! We help you by checking availability of your items at the following stores: Best Buy, Newegg, Footlocker")
    print("> 1. Choose the store you want to start checking.")
    print("> 2. Input your search item.")
    print("> 3. When we find your item is available, follow the link.")
    print("\nChoose the store you want to start checking : ")
    print("""
    1 : eBay 
    2 : Flight Club
    3 : Footlocker
    4 : Newegg
    5 : Help
    6 : ACTIVATE PROMPT BOT
    0 : Exit"""
            )
    choice = input("\nEnter your choice : ")
    
    if choice == '6':
        search_site = input("Select the store ('1-4') you would like PROMPT BOT to search : ")
        search_string = input("\nPaste URL : ")

        if search_site == '1':
            import ebay_scraper as eby
            t = threading.Timer(5.0, eby.check_item_from_ebay_link, args=(search_string,))
            t.start()
            return
        elif search_site == '2' :
            import flight_club_scraper as fcs
            t = threading.Timer(5.0, fcs.check_item_from_fc_link, args=(search_string,))
            t.start()
            return
        elif search_site == '3' :
            import footlocker_scraper as fot
            t = threading.Timer(5.0, fot.check_item_from_flocker_link, args=(search_string,))
            t.start()
            return
        elif search_site == '4' :
            import newegg_scraper as newegg
            t = threading.Timer(5.0, newegg.check_item_from_newegg_link, args=(search_string,))
            t.start()
            return
    if choice == '5': 
        print(helpdoc.helpdoc())  
    else:
        search_string = input("\nWhat would you like to search for? : ")
    
    if choice == '1':
        import ebay_scraper as eby
        eby.ebay_site_search('http://www.ebay.com/', search_string)
    elif choice == '2' :
        import flight_club_scraper as fcs
        fcs.fc_site_search('http://www.flightclub.com/', search_string)
    elif choice == '3' :
        import footlocker_scraper as fot
        fot.flocker_site_search('https://www.footlocker.com/', search_string)
    elif choice == '4' :
        import newegg_scraper as newegg
        newegg.newegg_site_search('https://www.newegg.com/', search_string)
    elif choice == '0':
        print('Thanks for checking out > prompt')
        exit()
    else:
        print('Invalid choice. Please enter a number between 1 and 5 or 0.')
    time.sleep(10)
    os.system('clear')
    main() #returns user to original screen for other search options


if __name__ == "__main__":
    main()


# def output():
#     stripped, prompts = parse_template(read_template("../assets/hitlist_template.txt"))

#     res = user_prompt(prompts)
#     f = open("../assets/output.txt", "w")
#     f.write(merge(stripped, res))
#     f.close()
#     print(merge(stripped, res))


# output()

# Kevin this is for the CSV output

# r = requests.request("GET", url, headers=headers, params=querystring)
# data = r.json()
# for p in data["plpView"]["products"]["products"]["product"]:
#     res.append(p)
# df = pd.json_normalize(res)
# df.to_csv("firstresults.csv")
