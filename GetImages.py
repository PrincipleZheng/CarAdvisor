import time

import requests as requests

with open('./data/rawData.csv', 'r') as f:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    for line in f.readlines():
        line = line.strip().split(',')
        picUrl = line[12]
        r = requests.get(picUrl, headers=headers)
        # download the image
        with open('./pics/' + str(line[0]) + '.png', 'wb') as i:
            i.write(r.content)
        print('Downloaded: ' + picUrl)
        # sleep for a second to avoid being banned
        time.sleep(0.5)
