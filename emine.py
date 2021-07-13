import json
dosya = open("emine.json","r", encoding="utf-8")

x=json.load(dosya)

for i in x["kimlik"].values():
    print(i)
