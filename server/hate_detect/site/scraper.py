import requests
import re
from bs4 import BeautifulSoup
import json


def scrape():
    link = 'https://boards.4channel.org/pol/'
    page = requests.get(link)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('blockquote', class_ = 'postMessage')

    scrapedtext = {}
    scrapedtext['posts'] = []  
    
    for item in results:
        item = re.sub(r'(>>\d{9})','', item.text)
        scrapedtext['posts'].append({
            'message': item
        })
    # print(scrapedtext)
    return scrapedtext
