import requests, time, datetime

url = 'https://comcast.com'


def checkInternet():
    down = 0
    currentTime = datetime.datetime.now()
    
    try:
        r = requests.get(url)
        print(str(currentTime) + " Connected")
    except:
        log = open("InternetLog.txt", "a")
        log.write(str(currentTime) + ' No Internet\n')
        log.close()
        print(str(currentTime) + ' No Internet')
        try:
            r = requests.get(url)
            print("Internet has come back")
        except:
            
            down += 1
        

while True:
    checkInternet()
    time.sleep(20)