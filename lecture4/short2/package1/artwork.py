import requests


def get_artist_work(artist, size):
    try:
        request = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist, "size": size}
        )
        request.raise_for_status()
    except requests.HTTPError:
        print("Could not complete request")
        return {}
    else:
        return request.json()
