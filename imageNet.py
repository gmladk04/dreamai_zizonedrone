from bs4 import BeautifulSoup
import numpy as np
import requests
import cv2
import PIL.Image
import urllib

page = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02708093")
soup = BeautifulSoup(page.content, 'html.parser')
str_soup = str(soup)
split_urls = str_soup.split('\r\n')
print(len(split_urls))
print(split_urls[0])

def url_download(urls, path, prefix) :
    idx = 0
    for url in urls:
        try:
            resp = urllib.request.urlopen(url)
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            if(len(image.shape)) == 3:
                print(url)
                idx += 1
                save_path = path + '/' + prefix + str(idx) + '.jpg'
                cv2.imwrite(save_path,image)
        except :
            None

url_download(split_urls, './clock', 'imageNet_clock(1)')