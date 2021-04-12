import requests
import pprint

url = 'https://pokeapi.co/api/v2'
query = ''

search = url + query

r = requests.get(search)

pp = pprint.PrettyPrinter()(width=41, compact=True)
pp.pprint(r.content)