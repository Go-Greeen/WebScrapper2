import requests
from bs4 import BeautifulSoup

bible_result = requests.get("https://www.desiringgod.org/search/results?utf8=%E2%9C%93&q=bible#gsc.tab=0&gsc.q=bible&gsc.page=1")
bible_soup = BeautifulSoup(bible_result.text, "html.parser")

print(bible_soup)
