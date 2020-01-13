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


path = os.path.dirname(os.path.realpath(__file__))
totpath = path+'\\webscrape_output'
fpath = totpath + '\\webscrape.txt'

if os.path.isdir(totpath) == True:
    f = open(fpath,'w+')
    for i in datalist:
        f.write(i)
    f.close()
else:
    os.mkdir(totpath)
    f = open(fpath,'w+')
    for i in datalist:
        f.write(i)
    f.close()
    
