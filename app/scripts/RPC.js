const { Client } = require('discord-rpc');
const clientId = '1138271149839634532';
const rpc = new Client({ transport: 'ipc' });
var path = require('path');
var jsonF = require(path.join(__dirname, 'config.json'));
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

rpc.on('ready', () => {
  console.log('Connected to Discord RPC');
});
rpc.login({ clientId }).catch(console.error);

// Get the config file
function getConfig(){
  fetch(path.join(__dirname, 'config.json'))
  .then((response) => response.json())
  .then((jsonF) => console.log(jsonF));
  const username = jsonF["username"];
  const api_key = jsonF["API_KEY"];
  const useSmallImage = jsonF["smallImagePP"];
  const displayScrobbles = jsonF["displayScrobbles"];
  const displayLyrics = jsonF["displayLyrics"];
  return [username, api_key, useSmallImage, displayScrobbles, displayLyrics];
}

// set the variables
const userData = getConfig();
username = userData[0];
api_key = userData[1];
useSmallImage = userData[2];
displayScrobbles = userData[3];
displayLyrics = userData[4];
const BaseURL = `https://www.last.fm/user/${username}`;
const URL = `http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=${username}&api_key=${api_key}&format=json`;
const profileInfo = `http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=${username}&api_key=${api_key}&format=json`;

// Get profile picture
async function getProfilePic()
{
  let response = await fetch(profileInfo);
  let data = await response.json();
  return data;
}

let smallImageURL = 'lastfm'

getProfilePic().then(data => {
  const profilePicUrl = data.user.image[2]['#text'];
  console.log(profilePicUrl); // Optional: Print the URL to verify
  if(useSmallImage)
  {
    smallImageURL = profilePicUrl;
  }
  // You can now use the 'profilePicUrl' variable elsewhere in your code
});


// Get the song data
async function getSongData() {
  try {
    let response = await fetch(URL);
    let data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching song data:', error);
    return null;
  }
}


let lastSong = null;

function updateBio(songTitle, songArtist)
{
  fetch(`http://127.0.0.1:5000/changeBio?songTitle=${songTitle}&songArtist=${songArtist}`)
  .then(response => {
    if (response == "Success") {
      console.log("Successfully updated bio")
    }
    return response.json(); // You may use response.text() if the server returns plain text
  })
}

function updatePresence() {
  (async () => {
    let scrobbles = 0;
    let artist = "";
    let song = "";
    let album = "";
    let image = "";
    let nowplaying = false;

    try {
      const data = await getSongData();
      if (data) {
        artist = data.recenttracks.track[0].artist['#text'];
        song = data.recenttracks.track[0].name;
        album = data.recenttracks.track[0].album['#text'];
        image = data.recenttracks.track[0].image[3]['#text'];

        try {
          nowplaying = data.recenttracks.track[0]['@attr'].nowplaying;
        } catch {
          nowplaying = false;
        }

        let scrobblesURL = `${BaseURL}/library/music/${artist.replace(' ', '+')}/_/${song.replace(' ', '+')}`;

        try {
          const response = await fetch(scrobblesURL);
          const html = await response.text();

          const dom = new JSDOM(html);
          const parser = new dom.window.DOMParser();
          const doc = parser.parseFromString(html, 'text/html');
          scrobbles = doc.querySelector('.metadata-display').textContent;
        } catch (error) {
          console.error('Error fetching scrobbles:', error);
        }

        console.log("Track: " + song);
        console.log("Artist: " + artist);
        console.log("Scrobbles: " + scrobbles);
        console.log("Album: " + album);
        console.log("Album-Cover: " + image);
        console.log("Playing: " + nowplaying);

        const songData = [song, artist, scrobbles, album, image, nowplaying];
        return songData;
      }
    } catch (error) {
      console.error('Error:', error);
    }
  })().then(songData => {
    // Here you can use the returned songData in your client.updatePresence call
    const [song, artist, scrobbles, album, image, nowplaying] = songData;
    
    if(nowplaying == false){
      console.log("Not playing")
      // Update the HTML elements with the fetched data
      document.getElementById("songName").textContent = 'Paused';
      document.getElementById("songArtist").textContent = '';
      document.getElementById("songAlbum").textContent = '';
      document.getElementById("albumPic").src = '';
      document.getElementById("songScrobbles").textContent = '';
      document.getElementById("status").textContent = "Status - Paused";
      rpc.clearActivity();
      return;
    }
    else
    {
      if(lastSong == song){
        console.log("Same song")
        return;
      }
      else
      {
        lastSong = song;
        if(displayScrobbles){
        setActivity(song, artist, image, album, smallImageURL, scrobbles);
        }
        else{
          setActivity(song, artist, image, album, smallImageURL, 'Last.FM');
        }

        // Update the HTML elements with the fetched data
        document.getElementById("songName").textContent = song;
        document.getElementById("songArtist").textContent = artist;
        document.getElementById("songAlbum").textContent = album;
        document.getElementById("albumPic").src = image;
        document.getElementById("songScrobbles").textContent = scrobbles;
        document.getElementById("status").textContent = "Status - Now Playing";
      }
    }
  });
}


function setActivity(song, artist, image, album, smallImageURL, scrobbles)
{
  if(displayLyrics){ updateBio(song, artist); }
  
  rpc.setActivity({
    details: `${song}`,
    state: `by ${artist}`,
    startTimestamp: new Date(),
    largeImageKey: `${image}`,
    largeImageText: `${album}`,
    smallImageKey: `${smallImageURL}`,
    smallImageText: `  ${scrobbles}`,
    instance: true,
    buttons: [{ label: "Github", url: `https://github.com/chubbyyb/LastFM-Discord-RPC`}, { label: "Last.FM", url: `https://www.last.fm/user/${username}`}]
  });
}

// Call the updatePresence function every 15 seconds
setInterval(updatePresence, 15000);
