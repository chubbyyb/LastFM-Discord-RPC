import requests
from bs4 import BeautifulSoup
import pypresence


BaseURL = "https://www.last.fm"
URL = "https://www.last.fm/user/Chubbyyb"

def getPage():
    # Get the HTML of the page
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    class_name = "chartlist-row chartlist-row--now-scrobbling chartlist-row--with-artist chartlist-row--with-buylinks js-focus-controls-container"
    elements = soup.find_all(class_=class_name)
    return elements

def getSongName():
    # Get the song name and artist name
    songName = getPage()[0].find(class_="chartlist-name").get_text()
    return songName.strip()

def getArtistName():
    artistName = getPage()[0].find(class_="chartlist-artist").get_text()
    return artistName.strip()

def getAlbumCoverURL():
    # Get the album cover
    albumCover = BaseURL + getPage()[0].find(class_="chartlist-image").find("a").get("href")
    albumCoverPage = requests.get(albumCover)
    albumCoverSoup = BeautifulSoup(albumCoverPage.content, 'html.parser')
    albumCoverURL = albumCoverSoup.find(class_="album-overview-cover-art js-focus-controls-container").find("img").get("src")
    return albumCoverURL.strip()

print(f"Song Name: {getSongName()}\nArtist Name: {getArtistName()}\nAlbum Cover: {getAlbumCoverURL()}")