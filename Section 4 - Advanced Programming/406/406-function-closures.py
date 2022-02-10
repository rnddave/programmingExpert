"""
Function Closures >>

tricky subject

"""

def outer(x, y):
    def nested():
        return x + y

    return nested

value = outer(1, 2)()
print(value)                    # OUTPUT >> 3

"""
Notes: 

functions are objects

nested functions

"""

def outer(x):
    def inner(y):
        print(x + y)

    return inner

print(outer(3))                 # <function outer.<locals>.inner at 0x10cdad670> == .locals = means local to the function

func = outer(5)                 # initially we pass a vlaue to outer
func(60)                        # now when we call our variable, we can pass another value (which will go into the nested function)
# 65 (x + y)

# alternatively, we can call it like so: 

outer(5)(4)                     # 9
# this passes the first (val) to first function and second (val) to the nested function
# we can have any number of nested functions for some unknown reason...

"""
closures

"free variables" = anything that is not local to the function you are using

Python makes this distinction because of closures. A free variable is not defined in the current environment, 
i. e. collection of local variables, and is also not a global variable! Therefore it must be defined elsewhere. 

If a variable is used in a code block but not defined there, it is a free variable.


"""


def collection(): 
    lst = []

    def inner(value): 
        lst.append(value)
        return lst

    return inner

add_value = collection()

print(add_value(1))
print(add_value(6))
print(add_value(9))

"""
[1]
[1, 6]
[1, 6, 9]

everytime we call add_value, we add a new item to the list

we're kind of mimicing the use of a class as follows


class Collection: 
    def __init__(self):
        self.lst2 = []

    def add_value(self, value):
        self.lst2.append(value)
        return self.lst2

"""

def counter(start):
    count = start

    def increment(value):
        nonlocal count          # makes this variable not local to this function,
                                # therefore reference the outer functions variable
                                # without this [nonlocal] keyword, this will not work,
                                # because we are trying to modify an immutable datatype
        count += value
        return count

    return increment

count = counter(2)
print(count(1))





