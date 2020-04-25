import requests
from bs4 import BeautifulSoup

limit = 5

url = "https://www.independent.ie/news/"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.92 Chrome/81.0.4044.92 Safari/537.36"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
headlines = soup.find_all("h4", limit = limit)

for i in range(0,limit):
    headlines[i] = headlines[i].get_text().rstrip()

def getN():
    return headlines