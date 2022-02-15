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

I modified my code FROM this: 

thread1 = threading.Thread(target=append_values, args=(lst, [1, 3, 5, 3], ))
thread2 = threading.Thread(target=append_integer, args=(lst, 4))

thread1.start()
thread2.start()
thread1.join()

TO THIS: 

thread1 = threading.Thread(target=append_values, args=(lst, [1, 3, 5,], ))
thread2 = threading.Thread(target=append_integer, args=(lst, 4))
thread3 = threading.Thread(target=append_values, args=(lst, [3], ))

thread1.start()
thread2.start()
thread1.join()
thread3.start()

OUTPUT is still correct - but still time out in playground, unsure why, 
I have instead used the example solution to move forward to next question

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

###################################
# 413.03 - Powers of 2 multithread
###################################

"""
POWERS OF TWO - MULTI-THREADED

- write program
- uses multiple threads to gather the ppowers of two included in a range

- program must use at least [2] threads, each responsible for part of the range

- you are given a function called [is_power_of_two] to start with
-- returns [True] if given number is power of 2
-- else [False]

"""

import threading

RANGE_START = 0
RANGE_END = 1000


def is_power_of_two(x):
    if x == 0:
        return False
    return (x & (x - 1)) == 0


powers_of_two = set()
set_lock = threading.Lock()


def find_powers_of_two(iter):
    for x in iter:
        if is_power_of_two(x):
            set_lock.acquire()                                                              # lock, ensure only one thread modify at a time
            powers_of_two.add(x)                                                            # add the new items to the [powers-of-two] thread
            set_lock.release()                                                              # release lock, allow next thread


thread1 = threading.Thread(target=find_powers_of_two, args=(range(RANGE_START, 250),))      # split the range up by quarters
thread2 = threading.Thread(target=find_powers_of_two, args=(range(250, 500),))
thread3 = threading.Thread(target=find_powers_of_two, args=(range(500, 750),))
thread4 = threading.Thread(target=find_powers_of_two, args=(range(750, RANGE_END),))

thread1.start()                                                                             # start them in order
thread2.start()
thread3.start()
thread4.start()

thread1.join()                                                                              # join the threads at end of work
thread2.join()
thread3.join()
thread4.join()