"""
often times you need to write a function that can accept a number of arguments, you may not always know what thumber will be

*args
**kwargs

"""

def pretty_print(*args, **kwargs):
    print("*" * 15)
    print(*args, **kwargs)
    print("*" * 15)


pretty_print(*["H", "e", "l", "l", "o", "world"], end="!\n")

# _+_+_+_+_+_+_+_+_+_+_

