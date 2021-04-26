import requests, time, datetime, signal

down = 0
totalDown = 0
increment = 2

def signal_handler(signum, frame):
    raise Exception(internetDown())

def internetUp():
    global down
    down = 0
    print('Internet is Up')

def internetDown():
    global down
    down += increment
    global totalDown
    totalDown += increment
    downTime = 'Current Downtime: ' + str(down) + ' seconds\nTotal Downtime: ' + str(totalDown) + ' seconds\n-------------------------------------'
    print(downTime)
    log = open("InternetLog.txt", "a")
    log.write(downTime)
    log.close()

def checkInternet():
    currentTime = datetime.datetime.now()
    
    try:
        r = requests.get('https://api.github.com/events')
        connected = str(r)
        
    except:
        log = open("InternetLog.txt", "a")
        entry = '\n' + str(currentTime) + ' No Internet\n'
        log.write(entry)
        log.close()
        
    if connected == '<Response [403]>' or '<Response [200]>':
        internetUp()

def writeLog():
    log = open("InternetLog.txt", "a")
    log.write(entry)
    
while True:
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(increment)   
    try:
        checkInternet()
    except:
        internetDown()
    time.sleep(increment)