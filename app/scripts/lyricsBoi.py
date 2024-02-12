import requests
from azapi import AZlyrics
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

MAXCHARS = 175 # Max characters for bio on Discord is 190, do not exceed this. Its 175 because of the "By LastFM-RPC" prefix

@app.route('/changeBio', methods=['GET'])
def changeBio():
    api = AZlyrics()

    api.title = request.args.get('songTitle')
    api.artist = request.args.get('songArtist')

    print(api.title)
    print(api.artist)

    api.getLyrics(save=False)

    lyrics = api.lyrics[:MAXCHARS]

    # Please go to --> https://curlconverter.com/python/
    cookies = {

    }

    headers = {

    }

    json_data = {
        'bio': f"By LastFM-RPC\n{lyrics}",
    }

    response = requests.patch('https://discord.com/api/v9/users/%40me/profile', cookies=cookies, headers=headers, json=json_data)

    if (response.status_code) == 200:
        return 'Success'
    else:
        return 'Error'
    

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"bio":"``🐸 pepe.exe                ⎯⠀❐⠀⤬ ``\\n   would you like to continue\\n     \\\\_\\\\_\\\\_\\\\_\\\\_\\\\_\\\\_\\\\_      \\\\_\\\\_\\\\_\\\\_\\\\_\\\\_\\\\_\\\\_\\n   |      yes       |   |      no      |\\n    ----------      ----------"}'.encode()
    #response = requests.patch('https://discord.com/api/v9/users/%40me/profile', cookies=cookies, headers=headers, data=data)


@app.route('/shutdown', methods=['POST', 'GET'])
def shutdown():
    os.kill(os.getpid(), 9)
    return 'Server shutting down...'


app.run(debug=True)
