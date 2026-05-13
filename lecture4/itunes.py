import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Invalid Format")


response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1]
)

o = response.json()


print(json.dumps(response.json(), indent=2))


for result in o["results"]:
    print(result["trackName"])
