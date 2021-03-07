import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"
try:
    with request.urlopen(src) as f:
        # res = f.read().decode('utf-8')
        data = json.load(f)
        Attr = data["result"]["results"]
        # print(Attr)
        with open("data.txt" , "w" , encoding="utf-8") as w:
            for att in Attr:
                sc = att["file"].split(".jpg")
                w.write(att["stitle"]+ ',' + att["longitude"] + ',' + att["latitude"] +','+ sc[0] +'.jpg'  +'\n')
except Exception as e:
        print(" Hello world ^___^")