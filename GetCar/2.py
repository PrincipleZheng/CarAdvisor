import requests
from bs4 import BeautifulSoup
url='https://www.dongchedi.com/auto/library/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x'
strhtml=requests.get(url)
src = strhtml.content
soup=BeautifulSoup(src,'html.parser')

data = soup.select('#__next > div.tw-flex > div.new-main.new > div > ul > li > div > a.series-card_name__3QIlf')
for i in data:
    print(i.get_text())