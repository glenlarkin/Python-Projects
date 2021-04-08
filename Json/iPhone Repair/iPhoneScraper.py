# Parses Apple's iPhone Model site to create a JSON containing specifications from each iphone model
# https://support.apple.com/en-us/HT201296

from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup

data = requests.get("https://support.apple.com/en-us/HT201296")

# opening up connection, grabbing the page
#uClient = uReq(myUrl)
#page_html = uClient.read()
#uClient.close()
soup = BeautifulSoup(data.text, 'html.parser')

# Html parsing


#grabs each iPhone
containers = soup.find(id="sections")
container = containers.findAll('div')

for data in container:
    iphoneName = data.find('h2', class_="")
    specs = data.find_all('div')
    print(specs)
    