import requests
from bs4 import BeautifulSoup
import urllib.request

ImagesURL = "https://www.last.fm/music/"

html = requests.get("https://kworb.net/itunes/").text
soup = BeautifulSoup(html, 'html.parser')

def downloadImages():
    block_texts = soup.find_all(class_='bl mp text')
    block_texts.pop(0)
    for block_text in block_texts:
        try:
            block_text = block_text.find_next('a')
            text = block_text.get_text()
            imgPage = requests.get(ImagesURL + text.replace(' ', '+') + '/+images')
            #print(ImagesURL + text.replace(' ', '+'))

            imgPageSoup = BeautifulSoup(imgPage.content, 'html.parser')
            LFMURL = imgPageSoup.find(class_='image-list').find_next('img').get('src')
            #print((imgPageSoup.find(class_='image-list').find_next('img').get('src')).replace('avatar170s', '770x0'))

            urllib.request.urlretrieve(LFMURL.replace('avatar170s', '770x0'), f"assets/{text}.png")
            print(f"Downloaded {text}.png")
        except:
            print(f"error with {text}")

def getNames():
    block_texts = soup.find_all(class_='bl mp text')
    block_texts.pop(0)
    for block_text in block_texts:
        try:
            block_text = block_text.find_next('a')
            text = block_text.get_text()
            print(text)
        except:
            print(f"error with {text}")

getNames()