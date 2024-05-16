import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

# making the http request
response = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])
# print(json.dumps(response.json()), indent=2)    # pythno convert json to dictionary


# grabbing the json object
object = response.json()
# printing out only the name of the song
for result in object["results"]:
    print(result["trackName"])
    