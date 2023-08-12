from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import getInfo


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

data = getInfo.getMusic()

@app.route('/songInfoAPI', methods=['GET'])
def getSongInfoAPI():
    global data
    data = getInfo.getMusic()
    song_data = {
        'SongName': data[1],
        'Album': data[2],
        'AlbumCover': data[3],
        'Artist': data[0],
        'Scrobbles': data[4]
    }
    return jsonify(song_data)

# This will be called by the backend to prevent too many API calls
@app.route('/songInfo', methods=['GET'])
def getSongInfo():
    song_data = {
        'SongName': data[1],
        'Album': data[2],
        'AlbumCover': data[3],
        'Artist': data[0],
        'Scrobbles': data[4]
    }
    return jsonify(song_data)
    

def shutdown_server():
    os.kill(os.getpid(), 9)

@app.route('/shutdown', methods=['POST', 'GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

app.run(debug=True)


