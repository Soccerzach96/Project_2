import unittest
import requests
import re
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl


def grab_headlines():
    #Your code here

    address = 'http://www.michigandaily.com/section/opinion'
    r = requests.get(address)
    soup = BeautifulSoup(r.text,'html.parser')

    most_read = soup.find_all('div', {'class': 'view-id-most_read'})[0]

    headlines = []

    for li in most_read.find_all(class_="item-list"):
        if li.a:
            headlines.append(li.a.text.replace("\n", "").strip())
        else:
            headlines.append(li.contents[0].strip())
        # headline = li.text
        # headlines.append(headline)
    print(headlines)