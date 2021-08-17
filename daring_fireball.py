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

# from footlocker_scraper import site3

from welcome import welcome

# f = Figlet(font="slant")
# print(f.renderText(">  prompt"))
# 
# print(
#     """> Welcome! We help you by checking availability of your items at the following stores:
# [BBY]Best Buy, [NWE]Newegg, [FOT]Footlocker
# > 1. Search for the item at one of the stores listed above.
#   2. Copy the URL from that search.
#   3. At the prompt, type the [store code], [search result URL for your item] and press [Enter]
# > <Coming Soon> [store code], [Search Result URL] <Enter>
# > <For Now> We took your keyword and applied that to the search on YouTube. Enjoy Searching…!
# """
# )

# from progress.bar import Bar
# 
# bar = Bar('Loading', max=20)
# for i in range (20):
#     # Any Task
#     bar.next()
# bar.finish()


# @click.group()
def main():
    """
    Simple CLI for querying
    """
    
    os.system("clear")
    print(welcome("> prompt"))
    print("\Welcome! We help you by checking availability of your items at the following stores: Best Buy, Newegg, Footlocker")
    print("> 1. Choose the stor you want to start checking.")
    print("> 2. Input your search item.")
    print("> 3. When we find your item is available, follow the link.")
    print("\nChoose the store you want to start checking : ")
    print("""
    1 : eBay 
    2 : Flight Club
    3 : Footlocker
    4 : Newegg
    5 : Help
    0 : Exit"""
            )
    choice = input("\nEnter your choice : ")
    search_string = input("\nWhat would you like to search for? : ")

    if choice == '1':
        import ebay_scraper as eby
        eby.ebay_site_search('http://www.ebay.com/', search_string)
    elif choice == '2' :
        import flight_club_scraper as fcs
        fcs.fc_site_search('http://www.flightclub.com/', search_string)
    elif choice == '3' :
        import footlocker_scraper as fot
        fot.flocker_site_search('http://www.footlocker.com/', search_string)
    elif choice == '4' :
        bby_scrapper()
    elif choice == '5' :
        help_doc()
    elif choice == '0':
        print('Thanks for checking out > prompt')
        exit()
    else:
        print('Invalid choice. Please enter a number between 1 and 5 or 0.')
    os.system("clear")



# @main.command()
# @click.argument("query")
# def search(query):
#     """This search query from YouTube Videos"""
#     url_format = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={}&type=video&key=AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"

#     # Search by ChannelID
#     # url_format = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=UCWr0mx597DnSGLFk1WfvSkQ&type=channelId&key=AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"
#     # url_format = "https://googleapis.com/books/v1/volumes"
#     query = "+".join(query.split())

#     query_params = {"q": query}

#     response = requests.get(url_format, params=query_params)

#     click.echo(response.json()["items"])


# @main.command()
# @click.argument("id")
# def get(id):
#     # api_key = "AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"
#     # channelId = "UCWr0mx597DnSGLFk1WfvSkQ"
#     """This will return information about videos based upon your query"""
#     url_format = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={}&type=video&key=AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"
#     base_video_url = "https://www.youtube.com/watch?v="
#     # Search by ChannelID
#     # url_format = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=UCWr0mx597DnSGLFk1WfvSkQ&type=channelId&key=AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"
#     # url_format = "https://www.googleapis.com/books/v1/volumes/{}"
#     click.echo(id)

#     response = requests.get(url_format.format(id))
#     click.echo(response.json())

    # with open('data.json', 'w') as f:
    # json.dump(extracted_data, f, indent=4)


# def parse(self, response):
#     with open("data_file.json", "w") as filee:
#         filee.write("[")
#         for index, quote in enumerate(response.css("div.quote")):
#             json.dump(
#                 {
#                     "text": quote.css("span.text::text").extract_first(),
#                     "author": quote.css(".author::text").get(),
#                     "tags": quote.css(".tag::text").getall(),
#                 },
#                 filee,
#             )
#             if index < len(response.css("div.quote")) - 1:
#                 filee.write(",")
#         filee.write("]")

# json_data = requests.get(url_format).json()
# json_status = json_data["status"]
# print("API Status: " + json_status)


#     inp = urllib.request.urlopen(url_format).read()
#     resp = json.load(inp)
#     vidID = resp["items"][0]["id"]["videoId"]

#     video_exists = False
#     with open("videoid.json", "r") as json_file:
#         data = json.load(json_file)
#         if data["videoID"] != vidID:
#             driver = webdriver.FireFox()
#             driver.get(base_video_url + vidID)
#             video_exists = True

#     if video_exists:
#         with open("videoid.json", "w") as jason_file:
#             data = {"videoId": vidID}
#             json.dump(data, json_file)

# try:
#     while True"
#     look


if __name__ == "__main__":
    main()

# def read_template(path):
#     with open(path) as text:
#         contents = text.read()
#         stripped_contents = contents.strip()
#         return stripped_contents


# def parse_template(text):
#     new = tuple(re.findall(r"\{(.*?)\}", text))
#     length = len(new)
#     for i in range(0, length):
#         if i == 0:
#             print(i)
#             new_text = text.replace(new[i], "")
#         else:
#             new_text = new_text.replace(new[i], "")
#     return new_text, new


# def user_prompt(words):
#     print("Please type a response to the prompt and press [ENTER]")
#     responses = []
#     for word in words:
#         responses.append(input(f"Type (a/an) {word}: "))
#     return responses


# def merge(strip, res):
#     length = len(res)
#     for i in range(0, length):
#         if i == 0:
#             story = strip.replace("{}", res[i], 1)
#         else:
#             story = story.replace("{}", res[i], 1)
#     return story


# def output():
#     stripped, prompts = parse_template(read_template("../assets/hitlist_template.txt"))

#     res = user_prompt(prompts)
#     f = open("../assets/output.txt", "w")
#     f.write(merge(stripped, res))
#     f.close()
#     print(merge(stripped, res))


# output()
