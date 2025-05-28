import requests
import sys
import json

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
res = response.json()


for track in res["results"]:
    print(track["trackName"])



