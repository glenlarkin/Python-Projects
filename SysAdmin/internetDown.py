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
    print('Current Downtime: ' + str(down) + ' seconds\nTotal Downtime: ' + str(totalDown) + ' seconds')

def checkInternet():
    currentTime = datetime.datetime.now()
    
    try:
        r = requests.get('https://api.github.com/events')
        connected = str(r)
        
    except:
        log = open("InternetLog.txt", "a")
        log.write(str(currentTime) + ' No Internet\n')
        print(str(currentTime) + ' No Internet')
        log.close()
        
    if connected == '<Response [403]>' or '<Response [200]>':
        internetUp()
    
while True:
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(10)   # Ten seconds
    try:
        checkInternet()
    except:
        internetDown()
    time.sleep(2)