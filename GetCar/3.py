import requests
import csv
from bs4 import BeautifulSoup
carNum = '260'
imgLink = 'https://www.dongchedi.com/auto/series/' + carNum
# imgLink = 'https://www.dongchedi.com/auto/series/score/260-x-x-x-x-x-x'
strhtml = requests.get(imgLink)
soup=BeautifulSoup(strhtml.text,'html.parser')
data = soup.select('#__next > div > div.new-main.tw-overflow-hidden.new > div.tw-relative.tw-z-10.tw-mt-16.tw-mb-27.md\:tw-mb-12.tw-gap-y-0.tw-gap-x-12.tw-h-466.md\:tw-h-488.xl\:tw-h-499.\32 xl\:tw-h-525 > div.tw-absolute.tw-left-1\/2.tw-top-34.tw-flex.tw-flex-col.tw-items-center.tw-w-full.tw-h-full.tw-transform.tw--translate-x-436.lg\:tw--translate-x-446.xl\:tw--translate-x-474.\32 xl\:tw--translate-x-501 > div > div > div:nth-child(36) > img')
# data = soup.select('#__next > div > div.new-main.new > div.jsx-3362002263.header-wrapper.tw-flex.tw-relative.tw-pb-24.tw-pl-30.lg\:tw-pb-33.xl\:tw-pb-40.tw-pr-24.xl\:tw-pr-30 > section.jsx-3362002263.tw-flex-1 > div > img.jsx-2173306956.style_carImg__18tQf')
for baseitem in data:
    print(baseitem)