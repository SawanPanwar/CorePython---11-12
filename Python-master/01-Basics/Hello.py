import threading
from threading import *

def hello(name):
    for i in range(1, 6):
        print("Hello", i , name)
    return

def hi(name):
    for i in range(1, 6):
        print("Hi", i, name)
    return

t1 = threading.Thread(target=hello, args=('Ram',))
t2 = threading.Thread(target=hello, args=('shyam',))

t1.start()
t2.start()