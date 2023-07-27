import requests
from datetime import datetime

web_url = "https://api.mangadex.org"
r = requests.get(
    f"{web_url}/manga",
    params={"title": "One Piece"}
)
print(r.json())
print([manga["id"] for manga in r.json()["data"]])
