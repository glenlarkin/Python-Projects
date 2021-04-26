import requests, time, datetime, signal

down = 0
totalDown = 0

def signal_handler(signum, frame):
    raise Exception(internetDown())

def internetUp():
    global down
    down = 0
    print('Internet is Up')

def internetDown():
    global down
    down += 2
    global totalDown
    totalDown += 2
    print('Internet has been down for: ' + str(down) + ' seconds\nTotal time down: ' + str(totalDown))

def checkInternet():
    print("starting checkinternet()")
    print('getting date')
    currentTime = datetime.datetime.now()
    
    try:
        print('trying comcast')
        r = requests.get('https://api.github.com/events')
        connected = str(r)
        
    except:
        print('exception caught')
        log = open("InternetLog.txt", "a")
        log.write(str(currentTime) + ' No Internet\n')
        print(str(currentTime) + ' No Internet')
        print('right b4 log close')
        log.close()
        print('log has closed')
        
    if connected == '<Response [403]>' or '<Response [200]>':
        
        internetUp()
    print('ending checkinternet()')



while True:
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(10)   # Ten seconds
    try:
        checkInternet()
    except:
        internetDown()
    time.sleep(2)