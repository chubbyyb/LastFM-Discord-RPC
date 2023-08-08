from pypresence import Presence
import time
import random
import getInfo

client_id = "1138271149839634532"
RPC = Presence(client_id)
RPC.connect()
prevSong = '-'


while True:
    songName = getInfo.getSongName()
    artistName = getInfo.getArtistName()
    albumCoverURL = getInfo.getAlbumCoverURL()
    print(artistName.replace(' ', '_').lower())
    if(songName == "NSP"):
        print("Nothing playing")
        RPC.clear()
    else:
        if(songName == prevSong): 
            print("Same song playing")
        else:
            print("New song playing")
            prevSong = songName
            RPC.update(
                large_image=f"{albumCoverURL}",
                large_text=f"{artistName}",
                small_image="lastfm",
                small_text=f"{getInfo.getScrobbles()} scrobbles",
                details=f"{songName}",
                state=f"by {artistName}",
                start=time.time(),
                buttons= [{"label": "Github","url":"https://github.com/chubbyyb/LastFM-Discord-RPC"}]
            )
    time.sleep(10)