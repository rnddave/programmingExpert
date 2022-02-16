"""
ASYNCHRONOUS PROGRAMMING

- perform multiple tasks simultaniously 

"""

import asyncio
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
        await  asyncio.sleep(delay)


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





