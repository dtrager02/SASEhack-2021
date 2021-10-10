import requests
import re
from bs4 import BeautifulSoup


def scrape():
    link = 'https://boards.4channel.org/v/'
    page = requests.get(link)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('blockquote', class_ = 'postMessage')

    for item in results:
        item = re.sub(r'(>>\d{9})','', item.text)
        print(item)
