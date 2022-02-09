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

# "*args        = star-args" 
# " **kwargs    = star-star-kwargs"

def sum_items():
    pass

"""
suppose you want to accept some arguments, but you don't know how many is the maximum that could be passed >>> 

sum_items(1,2,3, 4)
sum_items(1, 2)

"""

def sum_items(*args):                   # not required to use this "args" but is accepted norm in python
    print(sum(args))

sum_items(1, 2, 3, 4)                   # 10
sum_items(1, 2)                         # 3

# but what if you wanted to pass keyword arguments = **kwargs
# kwarg = keyWord Args

def sum_items2(*args, **kwargs):        # not required to use this "args" but is accepted norm in python
    print(sum(args))
    print(kwargs)

sum_items2(1, 4, 3, 5)                  # 13
sum_items2(1, 5)                        # 6
sum_items2(1, 4, 7, k=2, a=5, b= 7)     # 12
                                        # {'k': 2, 'a': 5, 'b': 7}
                                        # this creates a dictonary of key/value pairs

def sum_items3(a, b):
    return a + b

args = [4, 5]
x= sum_items3(args[0], args[1])
print(x)                                # 9

# but this would get very annoying if you had a large number of items to pass: 

def sum_items4(a, b, c):
    print(a, b, c)                      
    return a + b + c            

args = [12, 154, 93]

x = sum_items4(*args)                   # 12 154 93
print(x)                                # 259


