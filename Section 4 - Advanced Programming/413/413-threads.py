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

# now we will try waiting (using [ .join() ])

print()

from time import sleep

def run(content, delay=1):
    sleep(delay)
    print(content)


thread1 = threading.Thread(target=run, args=("run 1", 2))
thread2 = threading.Thread(target=run, args=("run 2", 1))

thread1.start()
print("here's the join ...")
thread1.join()
thread2.start()

"""
OUTPUT

here's the join ...
run 2
run 1
run 1
run 2
"""

print("\n\nnow we're going to use thread join on thread 2 as well\n")

def run(content, delay=1):
    sleep(delay)
    print(content)


thread1 = threading.Thread(target=run, args=("thread 1 with a 2 second delay", 2))
thread2 = threading.Thread(target=run, args=("thread 2 with a 1 second delay", 1))

thread1.start()
thread2.start()
print("here's the join ...")
thread1.join()

print("another join")
thread2.join()

print("all done")

"""
OUTPUT

now we're going to use thread join on thread 2 as well

here's the join ...
thread 2 with a 1 second delay
run 2                                       #### this is a left over from earlier piece of code!!! 
thread 1 with a 2 second delay
another join
all done
"""

# check number of active threads: 
print("\n\n >> number of active threads >> \n\n")
print(threading.active_count())                 # 1

# new examples
print("new example; 1,2,3,4,5 (print) \n\n")

##################################

import threading
from time import sleep

def print_values(values, delay): 
    for item in values :
        print(item)
        sleep(delay)

thread1 = threading.Thread(target=print_values, args=([1, 3, 5], 0.2))
thread2 = threading.Thread(target=print_values, args=([2, 4], 0.2))

thread1.start()
thread2.start()

"""
1
2
4
3
5
"""
# output is random, but we can modify this by changing delay: 
print()

thread3 = threading.Thread(target=print_values, args=([1, 3, 5], 0.2))
thread4 = threading.Thread(target=print_values, args=([2, 4], 0.3))

thread3.start()
thread4.start()

"""
OUTPUT messed up, delays crossing from earlier code: 

1       
2

1
2
4
3
3
4
5
5

I will modify above code to make it easier to read where things are in the output

"""

thread1 = threading.Thread(target=print_values, args=([1.1, 1.3, 1.5], 0.2))
thread2 = threading.Thread(target=print_values, args=([2.2, 2.4], 0.2))

thread1.start()
thread2.start()

print()

thread3 = threading.Thread(target=print_values, args=([3.1, 3.3, 3.5], 0.2))
thread4 = threading.Thread(target=print_values, args=([4.2, 4.4], 0.3))

thread3.start()
thread4.start()

"""
OUTPUT still messed up with earlier code interjecting: 

1
2

1
2
1.1
2.2

3.1
4.2
3
3
2.4
1.3
3.3
4
4.4
4
5
5
3.5
1.5

might need to implement mutex example, just to better see this output... 
"""

from threading import Thread, Lock

mutex = Lock()

mutex.acquire()
thread5 = threading.Thread(target=print_values, args=([5.1, 5.3, 5.5], 0.4))
thread6 = threading.Thread(target=print_values, args=([6.2, 6.4], 0.4))

thread5.start()
thread6.start()

print()

thread7 = threading.Thread(target=print_values, args=([7.1, 7.3, 7.5], 0.6))
thread8 = threading.Thread(target=print_values, args=([8.2, 8.4], 0.7))

thread7.start()
thread8.start()
mutex.release()

"""
OUTPUT = that didn't work...

1
2

1
2
1.1
2.2

3.1
4.2
5.1
6.2

7.1
8.2
4
3
3
1.3
2.4
3.3
6.4
7.3
5.3
4
8.4
4.4
5
5
1.5
3.5
7.5
5.5


instead I'll change the delays: 

thread5 = threading.Thread(target=print_values, args=([5.1, 5.3, 5.5], 0.4))
thread6 = threading.Thread(target=print_values, args=([6.2, 6.4], 0.4))

thread5.start()
thread6.start()

print()

thread7 = threading.Thread(target=print_values, args=([7.1, 7.3, 7.5], 0.6))
thread8 = threading.Thread(target=print_values, args=([8.2, 8.4], 0.7))
"""
# new output: 
"""
new example; 1,2,3,4,5 (print) 


1
2

1
2
1.1
2.2

3.1
4.2
5.1
6.2

7.1
8.2
1.3
3
4
3
2.4
3.3
4
4.4
3.5
5.3
6.4
1.5
5
5
7.3
8.4
5.5
7.5
"""

# let's trying a lock - cannot move forward without the lock (kind of what I tried, but didn't work.)

sleep(2)
print("let's try the lock\n\n")
from threading import Thread, Lock

mutex = Lock()

def t5(lock):
    print("starting t5")
    lock.acquire()
    sleep(1)
    print("t5")
    lock.release()

def t6(lock):
    print("starting t6")
    lock.acquire()
    sleep(1)
    print("t6")
    lock.release()

lock = Lock()
thread5 = Thread(target=t5, args=(lock, ))
thread6 = Thread(target=t6, args=(lock, ))

thread5.start()             # t1
thread6.start()             # t2

print()

"""
output ==== 

let's try the lock


starting t5
starting t6

t5
t6
"""