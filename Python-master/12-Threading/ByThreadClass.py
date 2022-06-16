import threading
from threading import *
class Hi(Thread):
    def run(self):
        for i in range(1, 6):
            print("Hii...", i)
t1 = Hi()
t1.start()

