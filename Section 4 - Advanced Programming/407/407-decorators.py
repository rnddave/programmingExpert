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

#######################

# there is a legacy way of doing this as well: 

def foo():
    print("foo")

foo = decorator(foo)            # this is legacy way of doing this

foo()

# now for some better ways of building decorators

###################################
# this is why we were introduced to *args and **kwargs first
###################################

def decorator2(func): 
    def wrapper(*args, **kwargs):                   # this allows us to take any number of arguents in
        print("Wrapper function called func!")
        result = func(*args, **kwargs)
        return result
        
    return wrapper

@decorator2
def foo(x, y, z=2):
    print(x, y, z)

foo(2, 3, 4)

"""
Wrapper function called func!
2 3 4
"""

# order matters

"""
when using mutiple decorators, the order in which you add them matters

"""
# practice 

###################################
# 407.03 - add one decorator
###################################
"""
write a decorator function named [add_one] that simply adds ne to the return value of any function it decorates

then use this function to decorate [add_values] function

def add_values(x, y):
    return x + y
"""

def add_one(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result += 1
        return result

    return wrapper


@add_one
def add_values(x, y):
    return x + y

# add_values(2, 3)
# print(add_values)

"""
my tests were unsuccessful, but I still added it to the code window and it passed all tests, solutions follow
"""
# solution 1
def add_one(func):
    def wrapper(x, y):
        return_value = func(x, y)       # strange that this one only takes in 2 parameters,
                                        # I thought it needed the *args, **kwargs
        return return_value + 1         # this is the next main difference

    return wrapper


@add_one
def add_values(x, y):
    return x + y

# solution 2
def add_one(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return return_value + 1         # again, main difference, cleaner code, less lines 

    return wrapper


@add_one
def add_values(x, y):
    return x + y


###################################
# 407.04 - print return value decorator
###################################
"""
write a decorator function named [print_return_value] that prints the return value of any function it decorates

your decorator should work on any function regardless of the number of paremeters
"""





