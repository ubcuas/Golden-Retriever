import os
import sys
import time

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

PATH_TO_WRITE = '/uas/gcomx/golden/images'
NGINX_URL = 'http://golden-nginx/' 
EXT1 = 'JPEG'
EXT2 = 'jpg'
wait = 1

while True:


    def check_status():
        retries = 0
        success = False
        while not success:
            try:
                urlopen(NGINX_URL, timeout=1)
                success = True
            except Exception as e:
                retries += 1
                print('Error! Waiting %s secs and re-trying...' % wait, flush=True)
                print(retries, flush=True)
                time.sleep(wait)


    def list_of_imgs(url):
        check_status()
        page = requests.get(url).text
        # print(page)
        soup = BeautifulSoup(page, 'html.parser')
        return [url + '/' + node.get('href') for node in soup.find_all('a') if (node.get('href').endswith(EXT1)
                                                                                | node.get('href').endswith(EXT2))]


    for file in list_of_imgs(NGINX_URL):
        img_name = file.split('/')[-1]
        absolute_path = os.path.join(PATH_TO_WRITE, img_name);

        if not os.path.exists(absolute_path):
            # print(file)
            img_data = requests.get(file).content

            with open(os.path.join(PATH_TO_WRITE, img_name), 'wb') as handler:
                handler.write(img_data)
    time.sleep(1)
