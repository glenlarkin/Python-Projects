import requests
from bs4 import BeautifulSoup as bs

githubUser = input('Input Github User: \n')
url = 'https://github.com/' + githubUser
r = requests.get(url)

soup = bs(r.content, 'html.parser')
profileImage = soup.find('img', {'alt' : 'Avatar'})['src']

print(profileImage)