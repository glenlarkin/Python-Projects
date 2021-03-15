import time

def timer():
    complete = False
    start = 0
    while complete != True:
        time.sleep(1)
        start += 1
        print(start)
        if start == 60:
            complete = True

timer()