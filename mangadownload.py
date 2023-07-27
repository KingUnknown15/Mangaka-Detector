import requests
import os

web_url = "https://api.mangadex.org"
author = "EIICHIRO ODA"
id = "a1c7c817-4e59-43b7-9365-09675a149a6f"
language = "pt-br"
group = "4f1de6a2-f0c5-4ac5-bce5-02c7dbb67deb"

data_path = f"Dataset/{author}"

r = requests.get(f"{web_url}/manga/{id}/feed",
                 params={"translatedLanguage[]": language, "excludedGroups[]": group})

test = [chapter["id"] for chapter in r.json()["data"]]
print(type(test[0]))

y = 0
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