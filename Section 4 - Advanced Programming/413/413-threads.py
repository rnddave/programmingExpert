"""
THREADS

- how does Python Threading work? 

>>>     Thread      
- flow of execution of your program
- default = single thread (main) = line by line

- trying to speed up using concurrency, try to run many threads at same time 

>>>     THREADING   
- [threading] package come pre-installed
-- contains functions and classes that allow you to create new threads and coordinate them 

- most important = [Thread] & [lock]

>>>     CONCURRENCY
- ability for parts of program / application / algorithm to exeecute simultaniously 

>>>     MUTEX
- MUtually EXclusive Lock
- controls access to a section of code
- typically used in multi-threaded programs when a section should execute one line at a time
- if one thread has thhe [mutex] al other threads must wait until MUTEX released 
-- before they can execute locked section of code

"""

import random
import time
from threading import Thread, Lock

mutex = Lock()

def loop(thread_name, n):
    for i in range(n):
        # Sleep for up to 20 milliseconds.

        time.sleep(random.randint(1, 20) / 1000)
        print(f"Thread {thread_name}: {i}")



# TODO: As an exercise, try to change this code to let
# t1 finish first before t2 starts running. (Hint: A
# mutex lock should do the trick)
t1 = Thread(target=loop, args=("t1", 10))
t2 = Thread(target=loop, args=("t2", 10))

t1.start()
t2.start()

t1.join()
t2.join()

"""
OUTPUT

Thread t2: 0
Thread t2: 1
Thread t2: 2
Thread t1: 0
Thread t1: 1
Thread t1: 2
Thread t2: 3
Thread t1: 3
Thread t1: 4
Thread t2: 4
Thread t1: 5
Thread t2: 5
Thread t2: 6
Thread t1: 6
Thread t1: 7
Thread t1: 8
Thread t2: 7
Thread t2: 8
Thread t1: 9
Thread t2: 9
"""
print()
# now I tried the Mutex lock:

import random
import time
from threading import Thread, Lock

mutex = Lock()

def loop(thread_name, n):
    for i in range(n):
        # Sleep for up to 20 milliseconds.
        mutex.acquire()
        time.sleep(random.randint(1, 20) / 1000)
        print(f"Thread {thread_name}: {i}")
        mutex.release()


# TODO: As an exercise, try to change this code to let
# t1 finish first before t2 starts running. (Hint: A
# mutex lock should do the trick)
t1 = Thread(target=loop, args=("t1", 10))
t2 = Thread(target=loop, args=("t2", 10))

t1.start()
t2.start()

t1.join()
t2.join()

"""
OUTPUT

Thread t1: 0
Thread t1: 1
Thread t1: 2
Thread t1: 3
Thread t1: 4
Thread t1: 5
Thread t1: 6
Thread t1: 7
Thread t1: 8
Thread t1: 9
Thread t2: 0
Thread t2: 1
Thread t2: 2
Thread t2: 3
Thread t2: 4
Thread t2: 5
Thread t2: 6
Thread t2: 7
Thread t2: 8
Thread t2: 9
"""
print()
# video notes: 

import threading            # try not to name your python files with same name as common python modules

def run(content):
    print("run")

thread1 = threading.Thread(target=run, args=("run 1",))
thread2 = threading.Thread(target=run, args=("run 2",))

thread1.start()
thread2.start()

print(type(thread1))        # <class 'threading.Thread'>

"""
OUTPUT

run 1
run 2
"""

# now we're going to add some delay to try and show threading
print()

from time import sleep

def run(content, delay=1):
    sleep(delay)
    print(content)


thread1 = threading.Thread(target=run, args=("run 1", 2))
thread2 = threading.Thread(target=run, args=("run 2", 1))

thread1.start()
thread2.start()

"""
OUTPUT

run 2
run 1
"""