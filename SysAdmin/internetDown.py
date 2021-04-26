import requests, time, datetime

def checkInternet():
    currentTime = datetime.datetime.now()
    
    try:
        r = requests.get('https://api.github.com/events')
        print(str(currentTime) + " Connected")
    except:
        print(str(currentTime) + ' No Internet')
        down += 1

while True:
    checkInternet()
    time.sleep(5)