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

"""
***************
H e l l o world!
***************
"""

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

args = [12, 154, 93]                    # list
x = sum_items4(*args)                   # 12 154 93
print(x)                                # 259

args2 = (12, 154, 93)                   # tuple
y = sum_items4(*args2)                  # 12 154 93
print(y)                                # 259

kwargs = {"a": 5, "c": 34, "b": 35}
z = sum_items4(**kwargs)                # the double ** = unpack a dictonary
print(z)

def sum_items5(p1, p2, a=None, b=None, c=None):
    print(p1, p2, a, b, c)
    return a + b + c + p1 + p2

args = [1, 2]
kwargs = {"a": 5, "c": 34, "b": 35}
x2 = sum_items5(*args, **kwargs)        # 1 2 5 35 34
print(x2)                               # 77

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def sum_items6():
    pass

# let us imagine you have many values: 

values = [1, 4, 5, 6, 2, 4, 2, 7, 4, 7, 4, 6, 345, 34]

# we can see the values with the print statement, but this also shows the list structure: 
print(values)       # [1, 4, 5, 6, 2, 4, 2, 7, 4, 7, 4, 6, 345, 34]

# so we want to get rid of the list, we could do: 

for val in values:
    print(val)

"""
1
4
5
6
2
4
2
7
4
7
4
6
345
34
"""
# but we don't want each item on own list, so we can start adding complexity: 

for val in values:
    print(val, end=" ")             # 1 4 5 6 2 4 2 7 4 7 4 6 345 34

###
print("\n\n - breaking the output up a bit \n")
###

# OR - we could just use *values, which will unpack the list as follows: 

print(*values)                      # 1 4 5 6 2 4 2 7 4 7 4 6 345 34

#### new example

def test(p1, *args, **kwargs):      # 3 at least one positional argument, any number of arguments, any number of keyword arguments
    print(p1, args, kwargs)

values = [1, 2, 3, 4]
kwargs = {"s": 1, "hello": 4}
test(4, *values, **kwargs)          # 4 (1, 2, 3, 4) {'s': 1, 'hello': 4}

# Exercise / Practice
###################################
# 403.02: what get's printed out?
###################################

print(*[1, 2, 3, 4], **{'end': "|", 'sep': "*"})

# no idea, so I ran it in code = 1*2*3*4|

"""
* [ unpacks each item the list] 1 2 3 4
** unpacks the dictionary, but the print function reads what is unpacked as follows

end = | (instead of the defaul \n)
sep = * (instead of the default " " (space))

ergo >> 1*2*3*4|
"""

###################################
# 403.03: *Args and **Kwargs
###################################

"""
write a function name [get_args_and_kwargs] that accept unlimited number of positional and keyword arguments
- return [True] if at least [4] total arguments and if keyword [num] exists, is a number and is larger than [5].
- otherwise return [False]

- also need to handle errors
"""

def get_args_and_kwargs(*args, **kwargs):
    number_of_args = len(args) + len(kwargs)
    num = kwargs.get("num", 0)

    if not isinstance(num, int) and not isinstance(num, float):
        return False

    return number_of_args >= 4 and num > 5