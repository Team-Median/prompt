from io import StringIO
from pyfiglet import Figlet
import re, click, urllib, json, time, requests
from requests.models import Response
from selenium import webdriver


f = Figlet(font="slant")
print(f.renderText(">  prompt"))

print(
    """> Welcome! We help you by checking availability of your items at the following stores:
[BBY]Best Buy, [NWE]Newegg, [FOT]Footlocker

> 1. Search for the item at one of the stores listed above.
  2. Copy the URL from that search.
  3. At the prompt, type the [store code], [search result URL for your item] and press [Enter]

> <Coming Soon> [store code], [Search Result URL] <Enter>

> <For Now> We took your keyword and applied that to the search on YouTube. Enjoy Searching…!
"""
)


@click.group()
def main():
    """
    Simple CLI for querying
    """
    pass


@main.command()
@click.argument("query")
def search(query):
    """This search query from YouTube Videos"""
    url_format = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={}&type=video&key=AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"

    # Search by ChannelID
    # url_format = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=UCWr0mx597DnSGLFk1WfvSkQ&type=channelId&key=AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"
    # url_format = "https://googleapis.com/books/v1/volumes"
    query = "+".join(query.split())

    query_params = {"q": query}

    response = requests.get(url_format, params=query_params)

    click.echo(response.json()["items"])


@main.command()
@click.argument("id")
def get(id):
    # api_key = "AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"
    # channelId = "UCWr0mx597DnSGLFk1WfvSkQ"
    """This will return information about videos based upon your query"""
    url_format = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={}&type=video&key=AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"
    base_video_url = "https://www.youtube.com/watch?v="
    # Search by ChannelID
    # url_format = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=UCWr0mx597DnSGLFk1WfvSkQ&type=channelId&key=AIzaSyAUuEmNYCYQcxsjztXWU14N5uqhW0lThD4"
    # url_format = "https://www.googleapis.com/books/v1/volumes/{}"
    click.echo(id)

    response = requests.get(url_format.format(id))
    click.echo(response.json())

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
