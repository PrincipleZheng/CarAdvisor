# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup
urls = [
        'https://www.dongchedi.com/auto/library/10,15-0-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',
        'https://www.dongchedi.com/auto/library/20,25-0-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',
        'https://www.dongchedi.com/auto/library/30,40-0-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',
        'https://www.dongchedi.com/auto/library/50,!1-0-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',

        'https://www.dongchedi.com/auto/library/20,25-1-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',
        'https://www.dongchedi.com/auto/library/30,40-1-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',
        'https://www.dongchedi.com/auto/library/50,!1-1-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',

        'https://www.dongchedi.com/auto/library/20,25-2-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',
        'https://www.dongchedi.com/auto/library/30,40-2-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',
        'https://www.dongchedi.com/auto/library/50,!1-2-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',

        'https://www.dongchedi.com/auto/library/50,!1-4-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x'
        ]

index = 1
f = open('rawData.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow((['index', 'name', 'type', 'price', 'score', 'displacement', 'horsepower', 'torque', 'length',
                      'width', 'height', 'wheelbase','imgLink']))
for url in urls:
    strhtml=requests.get(url)
    with open(r'HTML.html', 'w+', encoding='utf-8') as f:
        f.write(strhtml.text)
    soup=BeautifulSoup(strhtml.text,'html.parser')

    data = soup.select('#__next > div.tw-flex > div.new-main.new > div > ul > li > div > a.series-card_name__3QIlf')
    i=0
    for baseitem in data:
        score = 0
        i+=1
        carNum = baseitem.get('href').split('/')[3]
        # https: // www.dongchedi.com / auto / series / score / 157 - x - x - x - x - x - x
        link = 'https://www.dongchedi.com/auto/series/score/'+carNum+'-x-x-x-x-x-x'
        newstrhtml = requests.get(link)
        newsoup = BeautifulSoup(newstrhtml.text, 'lxml')
        newdata = newsoup.select('#__next > div > div.new-main.new > div.jsx-3362002263.header-wrapper.tw-flex.tw-relative.tw-pb-24.tw-pl-30.lg\:tw-pb-33.xl\:tw-pb-40.tw-pr-24.xl\:tw-pr-30 > section.jsx-3362002263.tw-flex-1 > div > div.jsx-2173306956.style_seriesScoreContent__wjWK0.tw-flex.tw-items-center.tw-mt-24.lg\:tw-mt-17.xl\:tw-mt-40.tw-h-104.tw-z-10 > div.jsx-2173306956.style_scoreContentRight__3F_2e.tw-flex-1.tw-flex.tw-items-center.tw-justify-between > ul:nth-child(2) > li:nth-child(2)')
        for newitem in newdata:
            score = newitem.get_text()
        imgLink = newsoup.select('#__next > div > div.new-main.new > div.jsx-3362002263.header-wrapper.tw-flex.tw-relative.tw-pb-24.tw-pl-30.lg\:tw-pb-33.xl\:tw-pb-40.tw-pr-24.xl\:tw-pr-30 > section.jsx-3362002263.tw-flex-1 > div > img.jsx-2173306956.style_carImg__18tQf')
        for thing in imgLink:
            img = thing.get('src')
        # https: // www.dongchedi.com / auto / params - carIds - x - 1145
        dataLink = 'https://www.dongchedi.com/auto/params-carIds-x-'+carNum
        strhtml = requests.get(dataLink)
        soup = BeautifulSoup(strhtml.text, 'lxml')
        name_data = soup.select(
            '#__next > div > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div.table_root__14vH_.table_head__FNAvn > div:nth-child(1) > div:nth-child(2) > div > h1 > a')
        for item in name_data:
            name = item.getText()

        price_data = soup.select(
            '#__next > div > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div')
        for item in price_data:
            price = item.getText()
            price = price.replace('万', '')

        displacement_data = soup.select(
            '#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(4) > div:nth-child(4) > div:nth-child(2) > div')
        for item in displacement_data:
            displacement = item.getText()

        horsepower_data = soup.select(
            '#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(4) > div:nth-child(11) > div:nth-child(2) > div')
        for item in horsepower_data:
            horsepower = item.getText()

        torque_data = soup.select(
            '#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(4) > div:nth-child(14) > div:nth-child(2) > div')
        for item in torque_data:
            torque = item.getText()

        length_data = soup.select(
            '#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div')
        for item in length_data:
            length = item.getText()

        width_data = soup.select(
            '#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div')
        for item in width_data:
            width = item.getText()

        height_data = soup.select(
            '#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > div')
        for item in height_data:
            height = item.getText()

        wheelbase_data = soup.select(
            '#__next > div.tw-flex > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > div')
        for item in wheelbase_data:
            wheelbase = item.getText()

        type_data = soup.select('#__next > div > div > div > div.configuration_wrapper__1ydsq > div.configuration_main__2NCwO > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div')
        for item in type_data:
            type = item.getText()
            if type.__contains__('SUV'):
                type = 'SUV'
            elif type.__contains__('MPV'):
                type = 'MPV'

        if score=='-':
            score = 0
        result={
            # "评分链接":link,
            # "数据链接":dataLink,
            "编号":index,
            "详细型号": name,
            "类型":type,
            "价格":price,
            "外观评分":score,
            "排量":displacement,
            "马力":horsepower,
            "扭矩":torque,
            "车长":length,
            "车宽":width,
            "车高":height,
            "轴距":wheelbase,
            "图片":img
        }

        print(result)
        # 2. 基于文件对象构建 csv写入对象
        if torque == '':
            continue
        csv_writer.writerow([index,name,type,price,score,displacement,horsepower,torque,length,width,height,wheelbase,img])
        index += 1
f.close()




