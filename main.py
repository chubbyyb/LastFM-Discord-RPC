from pypresence import Presence
import time
import random
import getInfo

client_id = "1138271149839634532"
RPC = Presence(client_id)
RPC.connect()


while True:
    songName = getInfo.getSongName()
    artistName = getInfo.getArtistName()
    albumCoverURL = getInfo.getAlbumCoverURL()
    print(artistName.replace(' ', '_').lower())
    RPC.update(
        large_image=f"{artistName.replace(' ', '_').lower()}",
        large_text=f"{artistName}",
        details=f"{songName} - {artistName}",
        state="Playing"
        #buttons= [{"label": "YTM","url":"https://music.youtube.com/"}, {"label": "YTM","url":"https://music.youtube.com/"}]
    )
    time.sleep(10)