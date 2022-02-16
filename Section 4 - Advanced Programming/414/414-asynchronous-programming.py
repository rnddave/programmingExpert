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

asyncio.run(main())             # this is how you run async code