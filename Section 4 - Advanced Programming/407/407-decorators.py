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


"""