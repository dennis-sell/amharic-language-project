from bs4 import BeautifulSoup

import requests

#starting url
url = "https://bible.org/foreign/amharic/exo_toc.htm"


r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data)

out = open("dump.txt", 'w')

links = []

for link in soup.find_all('a'):
    l = link.get('href')
    if l != None:
        links.append(l)

for link in links:
    r = requests.get("https://bible.org/foreign/amharic/" + link)
    data = r.text
    soup = BeautifulSoup(data)
    for p in soup.find_all('font'):
        print p.string.encode('utf-8')
