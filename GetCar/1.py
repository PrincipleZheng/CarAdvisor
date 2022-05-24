import requests
from bs4 import BeautifulSoup
datalink = 'https://www.dongchedi.com/auto/params-carIds-x-4865'
strhtml=requests.get(datalink)
soup=BeautifulSoup(strhtml.text,'lxml')
name_data = soup.select('#__next > div > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div.table_root__14vH_.table_head__FNAvn > div:nth-child(1) > div:nth-child(2) > div > h1 > a')
for item in name_data:
    print(item.getText())

price_data = soup.select('#__next > div > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div')
for item in price_data:
    print(item.getText())

displacement_data = soup.select('#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(4) > div:nth-child(4) > div:nth-child(2) > div')
for item in displacement_data:
    print(item.getText())

horsepower_data = soup.select('#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(4) > div:nth-child(11) > div:nth-child(2) > div')
for item in horsepower_data:
    print(item.getText())

torque_data = soup.select('#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(4) > div:nth-child(14) > div:nth-child(2) > div')
for item in torque_data:
    print(item.getText())

length_data = soup.select('#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div')
for item in length_data:
    print(item.getText())

width_data = soup.select('#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div')
for item in width_data:
    print(item.getText())

height_data = soup.select('#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > div')
for item in height_data:
    print(item.getText())

wheelbase_data = soup.select('#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > div')
for item in wheelbase_data:
    print(item.getText())
#
# data = soup.select('')
# for item in data:
#     print(item.getText())
#
# data = soup.select('')
# for item in data:
#     print(item.getText())