import requests
from bs4 import BeautifulSoup

def open_webpage(link, n):
    base_url = link
    for i in range(n):
        requests.get(base_url).content
        print('opened - ' + str(i));

open_webpage('http://www.zilina.sk/?page=ukazspravu&id=16918', 1000)