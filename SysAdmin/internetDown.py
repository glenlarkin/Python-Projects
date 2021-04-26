import requests, time, datetime, signal

down = 0

def signal_handler(signum, frame):
    raise Exception("Timed out!")

def checkInternet():
    print("starting checkinternet()")
    print('getting date')
    currentTime = datetime.datetime.now()
    
    try:
        print('trying comcast')
        r = requests.get('https://api.github.com/events')
        
    except:
        print('exception caught')
        log = open("InternetLog.txt", "a")
        log.write(str(currentTime) + ' No Internet\n')
        print(str(currentTime) + ' No Internet')
        print('right b4 log close')
        log.close()
        print('log has closed')
    print('ending checkinternet()')


while True:
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(10)   # Ten seconds
    try:
        checkInternet()
    except:
        print ("Timed out!")
    time.sleep(2)