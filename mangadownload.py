import requests
import os


web_url = "https://api.mangadex.org"

#PARAMETER SETTINGS

#Author for download path
author = "TITE KUBO"

#Manga ID and Settings for request
id = "239d6260-d71f-43b0-afff-074e3619e3de"
language = "en"
group = "4f1de6a2-f0c5-4ac5-bce5-02c7dbb67deb"

#Download Path
data_path = f"Dataset/{author}"

#Request for Manga Feed
r = requests.get(f"{web_url}/manga/{id}/feed",
                 params={"translatedLanguage[]": language, "excludedGroups[]": group})

#Taking Manga ID from API Response
test = [chapter["id"] for chapter in r.json()["data"]]


y = 0 #For enumerating the pages

#Requesting Chapters and Downloading Chapters
for chapter in test[:20]:
    x = requests.get(f"{web_url}/at-home/server/{chapter}")
    x_json = x.json()
    try:
        host = x_json["baseUrl"]
        chapter_hash = x_json["chapter"]["hash"]
        data = x_json["chapter"]["data"]

        for page in data[3:15]:
            y += 1
            z = requests.get(f"{host}/data/{chapter_hash}/{page}")
            y_num = str(y)+'.png'

            with open(os.path.join(data_path, y_num),mode="wb") as f:
                f.write(z.content)
    except:
        continue