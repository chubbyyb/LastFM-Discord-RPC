import os
import json

BASEURL = "https://www.last.fm/user/"

print("Welcome to the LastFM-Discord-RPC config setup")

username = input("\n\nPlease enter your LastFM username: ")
API_KEY = input("\nPlease enter your LastFM API key, you can get this at the LastFM API page (Check README.md on github): ")


config = {"username": username, "API_KEY": API_KEY}
with open("config.json","w") as f:
    json.dump(config,f)