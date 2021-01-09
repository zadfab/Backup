

# Python program to demonstrate
# sys.exit()


import sys

from threading import Thread
import time

def rn():
    while True:
        print("hello")
        time.sleep(5)

def stop():

    print("1.21312448395")
    rn(quit())


p1 = Thread(target = rn)
p2 = Thread(target = stop)

p1.start()
p2.start()
