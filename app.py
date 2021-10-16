import os
import sys
import time
import argparse

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


parser = argparse.ArgumentParser()
parser.add_argument('--path', default='/uas/golden/images')
parser.add_argument('--url', default='http://golden-nginx/')
parser.add_argument('--wait', default=1)
parser.add_argument('--ext1', default='JPEG')
parser.add_argument('--ext2', default='jpg')
io_args = parser.parse_args()

PATH_TO_WRITE = io_args.path
NGINX_URL = io_args.url
wait = io_args.wait
EXT1 = io_args.ext1
EXT2 = io_args.ext2

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