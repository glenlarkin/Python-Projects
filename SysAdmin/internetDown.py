import requests, time, datetime

down = 0

def checkInternet():
    currentTime = datetime.datetime.now()
    
    try:
        r = requests.get('https://api.github.com/events')
        print(str(currentTime) + " Connected")
    except:
        log = open("InternetLog.txt", "a")
        log.write(str(currentTime) + ' No Internet\n')
        log.close()
        print(str(currentTime) + ' No Internet')
        

while True:
    checkInternet()
    time.sleep(20)