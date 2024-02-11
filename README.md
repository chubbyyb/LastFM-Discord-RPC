# LastFM-Discord-RPC
![logo](assets/logo.png)<br />
This adds RPC to Discord from LastFM.<br />
It will show:
* Display currently listening to music from LastFM to Discord
* Display LastFM profile picture to rich presence (Optional)
* Display scrobble amount to rich presence (Optional)
* Display the current songs lyrics in your bio (Optional, Beta) [Please read](#lyrics)

<details>
<summary><a name="lyrics"></a><H2>Lyrics 🎤</H2></summary>
To activate lyrics
   <ul>
      <li> Go to Discord on your browser </li>
      <li> Press settings in Discord and go to the bio changing section </li>
      <li> Open inspect element </li>
      <li> Press the **Network** tab </li>
      <li> Change your bio to whatever </li>
      <li> A event called "Profile" should now be in the network section, right click it and copy as cCurl (Bash) </li>
      <li> Paste it into https://curlconverter.com/python/ </li>
      <li> Open lyricsBoy.py and paste the output of curlconverter into the cookies and headers section </li>
   </ul>
</details>
   
## Requirements 🛠️
1. Create a [LastFM API Key](https://www.last.fm/api/account/create)
2. Install the packaged version [here](https://github.com/chubbyyb/LastFM-Discord-RPC/releases/tag/v0.2)
3. Run ``lfmRPC.exe``
4. Press settings, input your username and API key
5. Restart the program

# Build 🛠️
I like using electronmon because it hot reloads, feel free to edit manually
1. ```bash
   npm install
   ```
2. ```bash
   npm install electronmon
   ```
3. ```
   npx electronmon .
   ```
   
 
## Images 🎵
![eg1](assets/eg1.png)<br />
![eg3](assets/eg3.png)<br />
> Using profile picture as small image<br />
![DiscordCanary_mxJ0OSuhNA](https://github.com/chubbyyb/LastFM-Discord-RPC/assets/79348344/e65be998-42d9-4132-a630-f587ed5f0b64)<br />

![electron_ViDA6PggFb](https://github.com/chubbyyb/LastFM-Discord-RPC/assets/79348344/b574a340-135f-44d0-93e8-a9b014021057)
![image](https://github.com/chubbyyb/LastFM-Discord-RPC/assets/79348344/fc20e5f6-0d4a-4447-8ce6-78b12e319517)



<details>
<summary>💽 Supported Platforms:</summary>
<ul>
<li>Anything that scrobbles to LastFM is supported</li>
<li>This extension scrobbles most of the major streaming platforms: https://chrome.google.com/webstore/detail/web-scrobbler/hhinaapppaileiechjoiifaancjggfjm</li>
</ul>
</details>