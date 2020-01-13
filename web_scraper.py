# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:44:25 2020

@author: ShivamBhatnagar
"""

# %% Imports
from bs4 import BeautifulSoup as bs
import requests

import os


# %% Scraping the web
myurls = [r'https://www.bbc.co.uk/news',r'https://edition.cnn.com/',r'https://www.dailymail.co.uk/home/index.html',r'https://www.independent.co.uk/']

datalist = []
for i in myurls:
    url = i
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    tag = 'title'
    tsoup = soup.find(tag)
    datalist.append(tsoup.text)


path = r'C:\Users\ShivamBhatnagar\projects\news_scrape\webscrape_output'
fpath = path + '\\webscrape.txt'

if os.path.isdir(path) == True:
    
    f = open(fpath,'w+')
    for i in datalist:
        f.write(i)
else:
    os.mkdir(path)
    f = open(fpath,'w+')
    for i in datalist:
        f.write(i)
    
