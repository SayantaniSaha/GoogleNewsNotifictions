# -*- coding: utf-8 -*-
"""

@author: Sayantani

"""
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from plyer import notification


url = "https://news.google.com/news/rss"
xml_data = urlopen(url).read()
urlopen(url).close()
    
sp = BeautifulSoup(xml_data, "xml")
news_list = sp.find_all('item')
news_list = news_list[0:10]

title = "Top News Headline of the Hour"


while True:
    for news in news_list:
        message = news.title.text + "Published on: " + news.pubDate.text
        notification.notify(title=title, message=message, timeout=20)
    time.sleep(3600)