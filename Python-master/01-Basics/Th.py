import threading
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(1, 6):
            print("Hello", i)

t1 = Hello()
t1.start()
