###################################
# 414.00 - 414 Assessment code
###################################

###################################
# 414.02 - Coroutine = what is?
###################################
"""
any function that can suspend its execution and resume later
"""

###################################
# 414.04 - Add One Async
###################################
"""
write function called [add_one]
- accept a coroutine as mandatory parameter
- calls the coroutine and returns value +1
"""

import asyncio

async def add_one(n):
    data = n + 1
    await asyncio.sleep(0.5)
    print(data)
    return data

async def main():

    task1 = asyncio.create_task(add_one(6))
    task2 = asyncio.create_task(add_one(43))

    await task1
    await task2

asyncio.run(main())

"""
>>> OUTPUT

7
44

This is what I expected

BUT DOES NOT WORK IN CODE PLAYGROUND!!!
"""