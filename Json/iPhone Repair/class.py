import json

data = json.loads(open('Json/iPhone Repair/iPhone.json').read())

class iPhone:
    def __init__(self, name, repairs):
        self.name = name
        self.repairs = repairs

    def matchUp(self):
        for items in data:
            print(items[0])

test = iPhone("iPhone x", "display")
test.matchUp()