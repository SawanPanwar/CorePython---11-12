import threading
from threading import *
import time

def first_thread():
    print("Hello First_Thread Daemon...")
    for i in range(1, 6):
     time.sleep(2)
     print("How are you First_Thread? daemon")

def second_thread():
    print("Hello Second_Thread")
    for i in range(1, 6):
     time.sleep(4)
     print("how are you Second_Thread?",i)

t1 = threading.Thread(target=second_thread)
t2 = threading.Thread(target=first_thread, daemon='true')


t1.start()
time.sleep(2)
t2.start()

