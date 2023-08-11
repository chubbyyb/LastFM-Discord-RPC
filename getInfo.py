import requests
import json
from bs4 import BeautifulSoup
import os


if os.path.exists("config.json") == False:
    print("Config file not found, please run setup.py")
    input("Press enter to quit")
    quit()

with open("config.json", "r") as f:
    config = json.load(f)

api_key = config["API_KEY"]
username = config["username"]
BaseURL = f"https://www.last.fm/user/{username}"
URL = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={api_key}&format=json"
profileInfo = f"http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user={username}&api_key={api_key}&format=json"


def getProfilePic():
    profileInfoJson = requests.get(profileInfo)
    profilePic = json.loads(profileInfoJson.text)['user']['image'][2]['#text']
    return profilePic


def getMusic():
    scrobbles = 0
    page = requests.get(URL)
    artist = json.loads(page.text)['recenttracks']['track'][0]['artist']['#text']
    songName = json.loads(page.text)['recenttracks']['track'][0]['name']
    album = json.loads(page.text)['recenttracks']['track'][0]['album']['#text']
    image = json.loads(page.text)['recenttracks']['track'][0]['image'][3]['#text']

    #try:
    #    trackInfo = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={api_key}&artist={artist.replace(' ', '+')}&track={songName.replace(' ', '+')}&format=json"
    #    duration = json.loads(requests.get(trackInfo).text)['track']['duration']
    #except:
    #   print("duration not found")

    # Check if now playing
    try: nowplaying = json.loads(page.text)['recenttracks']['track'][0]['@attr']['nowplaying']
    except: return ["NSP", "NSP", "NSP", "NSP", "NSP"]
    
    try:
        scrobblesURL = requests.get(BaseURL + "/library/music/" + artist.replace(' ', '+') + "/_/" + songName.replace(' ', '+')).text
        #print(URL + "/library/music/" + getArtistName().replace(' ', '+') + "/_/" + getSongName().replace(' ', '+'))
        scrobbles = BeautifulSoup(scrobblesURL, 'html.parser').find(class_="metadata-display").get_text()
    except:
        print("Scrobbles not found")
    
    return [artist.strip(), songName.strip(), album.strip(), image.strip(), scrobbles]



