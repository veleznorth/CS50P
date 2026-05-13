import requests


def get_artists(artist):
    try:
        request = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {"q": artist, "size": 3}
        )
        request.raise_for_status()
    except requests.HTTPError:
        print("Could not complete request")
        return {}
    else:
        return request.json()
