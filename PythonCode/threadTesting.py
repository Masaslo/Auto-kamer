import threading
import time

var = 0

def func1():
    while True:
        time.sleep(1)
        print(var)

def func2():
    global var
    while True:
        time.sleep(1)
        var += 1

thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)

thread1.start()
thread2.start()