import server
import threading
import time

def lichtAan():
    pass

def lichtUit():
    pass


def deurDicht():
    pass

def loop():
    while 1:
        print("1")
        time.sleep(1)

Thread1 = threading.Thread(target=server.maakServer())
Thread2 = threading.Thread(target=loop())
Thread1.start()
Thread2.start()
