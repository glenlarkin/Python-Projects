import requests
import json
import urllib.request
#from PIL import Image

url = 'https://randomfox.ca/floof/'
fox = requests.get(url)
json = json.loads(fox.content)
pic = json['image']
#im = Image.open(json['image'])
#im.show()
resource = urllib.request.urlretrieve(pic)
output = open('file01.jpg','wb')
output.write(resource.read())
output.close()