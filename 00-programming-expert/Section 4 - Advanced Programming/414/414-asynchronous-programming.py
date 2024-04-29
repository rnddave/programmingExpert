"""
ASYNCHRONOUS PROGRAMMING

- perform multiple tasks simultaniously 

"""

import asyncio
from re import I
import time


# Here we fake the download of a large file by sleeping 1 second.
async def download_large_file(file_name):
    await asyncio.sleep(1)
    print(f"{file_name} was downloaded successfully")
    return f"{file_name}: OK"


# These are the files to download. Since each file takes 1 second
# to download, it would take 5 seconds without using asyncio.
FILES_TO_DOWNLOAD = [
    "textures.zip",
    "models.zip",
    "physics_engine.exe",
    "game.exe",
    "achievements.exe",
]


async def main():
    start_time = time.time()
    downloads = [download_large_file(file_name) for file_name in FILES_TO_DOWNLOAD]
    download_statuses = await asyncio.gather(*downloads)
    total_time = time.time() - start_time
    print(f"Finished downloading {len(download_statuses)} files in {total_time} seconds!")


asyncio.run(main())

"""
OUTPUT >>>

textures.zip was downloaded successfully
models.zip was downloaded successfully
physics_engine.exe was downloaded successfully
game.exe was downloaded successfully
achievements.exe was downloaded successfully
Finished downloading 5 files in 1.0020651817321777 seconds!
"""

# moving on

"""
but what's synchronous programming? 
- sequential
- limited by speed of the processor (per core)

"""
# lets code

import asyncio                  # alternative to threading, easier to use and understand 
                                # advanced event scheduler, avoid spawning multiple threads 

async def print_something():
    await asyncio.sleep(1)
    print("something")

async def main():               # note this is a new keyword!!
    print("main")
    await print_something()     # this is 'blocking code' have to wait for it to finish
    print("main again")

asyncio.run(main())             # this is how you run async code
# print(type(main()))           # <class 'coroutine'>

"""
output

main
something
main again
"""
# let's talk about tasks (scheduling)


async def print_something():
    await asyncio.sleep(1)
    print("something")

async def main():               
    print("main")
    
    task = asyncio.create_task(print_something())     
                                # this will start the task before it waits
    print("main again")

asyncio.run(main())             # this is how you run async code

"""
OUPUT

main
main again                      # as you can see, it did not wait for the 'print_something' to complete before moving to next code block
"""
print()
# await task

async def print_something():
    await asyncio.sleep(1)
    print("something")

async def main():               
    print("main")
    
    task = asyncio.create_task(print_something())     
    
    print("main again")
    await task
    print("awaited")

asyncio.run(main()) 

"""
OUTPUT 

main
main again
something
awaited
"""

# let's pass a result this time 
print()

async def print_something():
    await asyncio.sleep(1)
    print("something")
    return "finished"                               # note this is the return

async def main():               
    print("main")
    
    task = asyncio.create_task(print_something())     
    
    print("main again")
    result = await task                             # wait for the return?
    print(result)                                   # print the return

asyncio.run(main()) 

"""
OUTPUT

main
main again
something
finished                                            # the returns
"""
# new example
print()

async def print_values(values, delay):
    for item in values:
        print(item)
        await  asyncio.sleep(delay)


async def main():
    await print_values([1.1, 1.3, 1.5],0.2)
    await print_values([1.2, 1.4], 0.3)

asyncio.run(main())

"""
OUTPUT

1.1
1.3
1.5
                                                    # why this output?
                                                    # because we 'await' X before Y can begin,
                                                    # so the delay on the Y is irrelevent as it was told to wait before following code block
1.2
1.4
"""

# let's scheule tasks instead
print()

async def print_values(values, delay):
    for item in values:
        print(item)
        await  asyncio.sleep(delay)                 # this works, because as soon as we 'sleep' we pass control back to other task


async def main():
    task1 = asyncio.create_task(print_values([2.1, 2.3, 2.5],0.2))
    task2 = asyncio.create_task(print_values([2.2, 2.4], 0.3))

    await task1
    await task2
    
asyncio.run(main())

"""
OUTPUT 

2.1
2.2
2.3
2.4
2.5
"""

# gathering tasks
print()

async def print_values(values, delay):
    for item in values:
        print(item)
        await  asyncio.sleep(delay)                 # this works, because as soon as we 'sleep' we pass control back to other task

        return delay

async def main():
    values = await asyncio.gather(print_values([3.1, 3.3, 3.5], 0.2), print_values([3.2, 3.4], 0.3))

    print(values)
   
asyncio.run(main())

"""
OUTPUT

3.1
3.2
[0.2, 0.3]

this is not as expected (expected all values to print)
"""

# new example
print()

async def fetch_data():
    print("start fetchhing")
    await asyncio.sleep(2)
    print("fetching complete")
    return [4.1, 4.2, 4.3, 4.4, 4.5, 4.6]

async def run_algerithm():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    data = await asyncio.gather(fetch_data(), run_algerithm()
    )

asyncio.run(main())

"""
>>> OUTPUT

start fetchhing
0
1
2
3
fetching complete
4
5
6
7
8
9
"""

# but what if we want one to complete before the other?
print()

async def fetch_data():
    print("start fetchhing")
    await asyncio.sleep(2)
    print("fetching complete")
    return [5.1, 5.2, 5.3, 5.4, 5.5, 5.6]

async def run_algerithm():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    data = await fetch_data() 
    await run_algerithm()
    

asyncio.run(main())

"""

>>> OUTPUT

start fetchhing
fetching complete
0
1
2
3
4
5
6
7
8
9
"""

# fetching data as well
print()

async def fetch_data():
    print("start fetchhing")
    await asyncio.sleep(2)
    print("fetching complete")
    return [6.1, 6.2, 6.3, 6.4, 6.5, 6.6]

async def run_algerithm():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    data = asyncio.create_task(fetch_data())
    await run_algerithm()
    print(await data)
    

asyncio.run(main())

"""
>>> OUTPUT

0
start fetchhing
1
2
3
fetching complete
4
5
6
7
8
9
[6.1, 6.2, 6.3, 6.4, 6.5, 6.6]
"""

"""
MORE NOTES >>> 

create a task =  futures 

essentially - in the future this will run and return value etc 

"""

# async generator 
print()

import asyncio

async def gen(n):
    for i in range(n):
        yield i
        await asyncio.sleep(0.5)

async def main():
    async for i in gen(10):
        print(f"7.{i}")

asyncio.run(main())

"""
>>> OUTPUT 


7.0
7.1
7.2
7.3
7.4
7.5
7.6
7.7
7.8
7.9
"""