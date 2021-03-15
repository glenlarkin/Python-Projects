import json

iPhones = json.loads(open('Json/iPhone Repair/iPhone.json').read())


print(iPhones["iPhones"][1]["name"])
cat = iPhones
