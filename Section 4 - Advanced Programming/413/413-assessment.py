"""assessment file for 413 - this is a tricky subject.... 


HINTS: 

Locks, Delays, .join()
"""

###################################
# 413.01 - output of following code:
###################################

import threading
from time import sleep

def t1():
    sleep(1)
    print("thread 1")

def t2():
    print("thread 2")
    sleep(1)

def t3():
    sleep(2)
    print("thread 3")

thread1 = threading.Thread(target=t1)
thread2 = threading.Thread(target=t2)
thread3 = threading.Thread(target=t3)
thread1.start()
thread2.start()
thread3.start()