import requests, time, datetime, signal

downTime = 0
totalDownTime = 0
increment = 2

def signal_handler(signum, frame):
    raise Exception(internetDown())

def internetUp():
    global downTime
    downTime = 0
    print('Internet is Up')

def internetDown():
    global downTime
    downTime += increment
    global totalDownTime
    totalDownTime += increment
    downTimeMsg = 'Current Downtime: ' + str(downTime) + ' seconds\nTotal Downtime: ' + str(totalDownTime) + ' seconds\n-------------------------------------'
    print(downTimeMsg)
    log = open("InternetLog.txt", "a")
    log.write(downTimeMsg)
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
    signal.alarm(5)   
    try:
        checkInternet()
    except:
        internetDown()
    time.sleep(increment)