from pypresence import Presence
import time
import random
import requests
#import getInfo

client_id = "1138271149839634532"
RPC = Presence(client_id)
RPC.connect()
prevSong = '-'
#profilePic = getInfo.getProfilePic()


while True:
    try:
        musicInfo = requests.get("http://localhost:5000/songInfoAPI").json()
        print(musicInfo)
        songName = musicInfo['SongName']
        artistName = musicInfo['Artist']
        albumName = musicInfo['Album']
        albumCoverURL = musicInfo['AlbumCover']
        scrobbles = musicInfo['Scrobbles']
    except:
        songName = "NSP"

    if(songName == "NSP"):
        print("Nothing playing")
        RPC.clear()
    else:
        if(songName == prevSong): 
            print(f"Same song playing - {songName}")
        else:
            if(albumCoverURL == ''):
                albumCoverURL = 'lastfm'
            print(f"New song playing - {songName}")
            prevSong = songName
            RPC.update(
                large_image=f"{albumCoverURL}",
                large_text=f"{albumName}",
                #small_image=f"{profilePic}",
                small_text=f"{scrobbles} scrobbles",
                details=f"{songName}",
                state=f"by {artistName}",
                start=time.time(),
                buttons= [{"label": "Github","url":"https://github.com/chubbyyb/LastFM-Discord-RPC"}]
            )
    time.sleep(10)
    

