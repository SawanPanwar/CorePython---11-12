import threading
import time
from threading import *

def Hello():
    for i in range(1, 6):
        time.sleep(5)
        print("Hello",i)

t1 = threading.Thread(target=Hello, daemon='true')

t1.start()

