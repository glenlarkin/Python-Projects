import requests, time

try:
    r = requests.get('https://api.github.com/events')
    print("Connected")
except:
    print('No Internet')

