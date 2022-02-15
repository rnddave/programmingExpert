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

"""
my guess = 
2
1
3

= CORRECT!! 
"""

###################################
# 413.02 - Starting Threads
###################################

"""
start, stop, join the existing functions as threads

such that
[ lst = [1, 4, 3, 5, 3] ]

starting code: 

import threading
from time import sleep
import math


def append_values(lst, values=[], delay=1):
    for value in values:
        lst.append(value)
        sleep(math.ceil(abs(delay)))


def append_integer(lst, integer):
    lst.append(integer)


lst = []
"""

import threading
from time import sleep
import math


def append_values(lst, values=[], delay=1):
    for value in values:
        lst.append(value)
        sleep(math.ceil(abs(delay)))
        #print(lst)


def append_integer(lst, integer):
    lst.append(integer)
    #print(lst)


lst = []
#print(lst)

thread1 = threading.Thread(target=append_values, args=(lst, [1, 3, 5,], ))
thread2 = threading.Thread(target=append_integer, args=(lst, 4))
thread3 = threading.Thread(target=append_values, args=(lst, [3], ))

thread1.start()
thread2.start()
thread1.join()
thread3.start()




print(lst)          # [1, 4, 3, 5, 3]

"""
OUTPUT = [1, 4, 3, 5, 3]

however, when I run it in the programmingExpert.io code playground, it fails with a code timeout error

RE-READ the problem - need at least 3 threads to pass, 
-- but don't know why not having three would generate a timeout error

"""

###################################
# 413.02 - Starting Threads - SOLUTION
###################################
"""
import threading
from time import sleep
import math


def append_values(lst, values=[], delay=1):
    for value in values:
        lst.append(value)
        sleep(math.ceil(abs(delay)))


def append_integer(lst, integer):
    lst.append(integer)


lst = []

# Write your code here.

thread1 = threading.Thread(target=append_values, args=(lst, [1, 3, 5], 1))
thread2 = threading.Thread(target=append_integer, args=(lst, 4))
thread3 = threading.Thread(target=append_integer, args=(lst, 3))
thread1.start()
thread2.start()
thread1.join()
thread3.start()
"""