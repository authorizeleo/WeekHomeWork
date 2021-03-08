import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
try:
    with request.urlopen(src) as f:
        # res = f.read().decode('utf-8')
        data = json.load(f)
        Attr = data["result"]["results"]
        # print(Attr)
        with open("data.txt" , "w" , encoding="utf-8") as w:
            for att in Attr:
                sc = att["file"].split("http")
                w.write(att["stitle"]+ ',' + att["longitude"] + ',' + att["latitude"] +',http'+ sc[1]  +'\n')
except Exception as e:
        print(" Hello world ^___^")
