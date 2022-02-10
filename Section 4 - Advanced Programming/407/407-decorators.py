"""
Decorators

common use is the @timer which is used for timing how long a a function took to complete for example, 

but essentially the @ is a decorator


"""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        total_time = end_time - start_time
        print(f"Time taken to execute: {total_time * 1000000} microseconds")
        return result

    return wrapper


def print_arguments(func):
    def wrapper(*args, **kwargs):
        print("Args:", args, "Kwargs:", kwargs)
        result = func(*args, **kwargs)
        return result

    return wrapper


def ignore_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Exception ignored:", e)
        return None

    return wrapper


@print_arguments
@ignore_exception
@timer
def loop(n):
    if n > 10000:
        raise Exception("n is too large to loop through!")
    for i in range(n):
        pass


loop(12)
loop(1000000)

"""
OUTPUT >>>

Args: (12,) Kwargs: {}
Time taken to execute: 0.95367431640625 microseconds
Args: (1000000,) Kwargs: {}
Exception ignored: n is too large to loop through!
"""

"""
these are functions, used to call other functions (??)

sit on top of a function
- take it in
- perform checks
- then call it

behind the scenes python magic 

decorator uses a nested function
"""

def decorator(func): 
    def wrapper():          # this needs to take the same as the function as parameters
        print("Wrapper function called func!")
        result = func()
        return result
        
    return wrapper

@decorator
def foo():
    print("foo")

foo()
"""
Wrapper function called func!
foo
"""

# what's going on here? 
"""
foo()
get's passed to decorator
"""

# we use this to either:

"""
>> enforce some behaviour 
>> to do something before or after the function was run
"""









