import requests
from bs4 import BeautifulSoup


BaseURL = "https://www.last.fm"
URL = "https://www.last.fm/user/Chubbyyb"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0', "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}



def getPage():
    # Get the HTML of the page
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    class_name = "chartlist-row chartlist-row--now-scrobbling chartlist-row--with-artist chartlist-row--with-buylinks js-focus-controls-container"
    elements = soup.find_all(class_=class_name)
    return elements

def getSongName():
    # Get the song name and artist name
    try:
        songName = getPage()[0].find(class_="chartlist-name").get_text()
        return songName.strip()
    except:
        return "NSP"

def getArtistName():
    try:
        artistName = getPage()[0].find(class_="chartlist-artist").get_text()
        return artistName.strip()
    except:
        return "NSP"

def getAlbumCoverURL():
    # Get the album cover
    try:
        albumCover = BaseURL + getPage()[0].find(class_="chartlist-image").find("a").get("href")
        albumCoverPage = requests.get(albumCover)
        albumCoverSoup = BeautifulSoup(albumCoverPage.content, 'html.parser')
        albumCoverURL = albumCoverSoup.find(class_="album-overview-cover-art js-focus-controls-container").find("img").get("src")
        return albumCoverURL.strip()
    except:
        return "NSP"
    
def getScrobbles():
    try:
        scrobblesURL = requests.get(URL + "/library/music/" + getArtistName().replace(' ', '+') + "/_/" + getSongName().replace(' ', '+')).text
        #print(URL + "/library/music/" + getArtistName().replace(' ', '+') + "/_/" + getSongName().replace(' ', '+'))
        scrobbles = BeautifulSoup(scrobblesURL, 'html.parser').find(class_="metadata-display").get_text()
        print(scrobbles)
        return scrobbles.strip()
    except:
        return "NSP"

print(f"Song Name: {getSongName()}\nArtist Name: {getArtistName()}\nAlbum Cover: {getAlbumCoverURL()}\nScrobbles: {getScrobbles()}")