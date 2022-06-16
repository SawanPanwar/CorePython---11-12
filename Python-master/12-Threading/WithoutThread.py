import threading
from threading import *
def hello(name , n):
    for i in range(1, 5):
        print("Hello", i, name, n)
    return


t1 = threading.Thread(target=hello, args= ("ram", "shayam"))
#t2 = threading.Thread(target=hello, args= ("shyam",))

t1.start()
#t2.start()
