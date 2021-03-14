import json

iPhones = json.loads(open('Json/iPhone Repair/iPhone.json').read())


print(iPhones[1]["name"])
cat = iPhones
