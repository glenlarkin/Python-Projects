import json

data = json.loads(open('Json/iPhone Repair/iPhone.json').read())
iPhones = data["iPhones"]

class Repair:
    def __init__(self, name, type, time, note):
        self.name = name
        self.type = type
        self.time = time
        self.note = note

    
testSubject = iPhones[4]["name"]
testRepair = iPhones[4]["repair"][2]

test = Repair(testSubject, testRepair, '23', 'nothing')
print(test.name, test.type)