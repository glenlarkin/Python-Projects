#! python3
#findHondaBikesKSL - scrapes Ksl Classified to find honda motorcycles for cheap

import requests
from bs4 import BeautifulSoup

URL = 'https://classifieds.ksl.com/search/Recreational-Vehicles/Motorcycles-Road-Bikes-Used/keyword/honda/priceTo/1000'
page = requests.get(URL).content(pprint())

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='lisings:')
print(results.prettify())
