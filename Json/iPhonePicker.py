import json

iPhones = json.loads(open('Json/iPhone Repair/iPhone.json').read())
inside = iPhones["iPhones"]

for phones in inside:
    name = phones["name"]
    repairs = phones["repairs"]
    print(name,repairs)