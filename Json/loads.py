import json

x = '{ "name":"Glen", "age":25, "city":"Salt Lake City"}'

y = json.loads(x)

print(y["name"])