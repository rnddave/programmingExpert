digits = [i for i in range(10)]
print(digits)

even_numbers = [i for i in range(20) if i % 2 == 0]
print(even_numbers)

divisible_by_3 = {i: i % 3 == 0 for i in range(30)}
print(divisible_by_3)

x, y = 13, "hello"
print(f"x = {x}, y = {y}")

x = y = 10
print(x, y)

########  Comprehensions
# example building a populated list in a single line of code

lst = [i for i in range(1,11)]
print(lst)                      # for every iteration of the for loop, add a new item within the range

lst = [i / 2 for i in range(1, 11) if i % 2 == 0]
print(lst)                      # [1.0, 2.0, 3.0, 4.0, 5.0]

# nested for loops in a single line (comprehension)

lst = [i * j for i in range(1, 11) for j in range(5)]
print(lst)                      # [0, 1, 2, 3, 4, 0, 2, 4, 6, 8, 0, 3, 6, 9, 12, 0, 4, 8, 12, 16, 0, 5, 10, 15, 20, 0, 6, 12, 18, 24, 0, 7, 14, 21, 28, 0, 8, 16, 24, 32, 0, 9, 18, 27, 36, 0, 10, 20, 30, 40]

##### this doesn't work for tuples, but does work for sets and dictionaries

s = {i * j for i in range(1, 11) for j in range(5)}
print(s)                        # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 27, 28, 30, 32, 36, 40}

dic = {i : j for i in range(1, 11) for j in range(5)}
print(dic)                      # {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4}

#### above is basics on comprehension 

#################

#### ##### MULTIPLE ASSIGNMENT

x = y = 1                       # basically assign two variables at the same time with the same value 
print(x, id(x), y, id(y))       # 1 4308465968 1 4308465968

x, y = 1, 2                     # this uses 1 line of code to assign multiple variables with different starting values 
print(x, id(x), y, id(y))

#### UNPACKING
# taking an iterable object (tuple, list) into individual items 

x, y = (1, 2)                     # number of variables = equal to number of items
print(x, id(x), y, id(y))

#### Docstring
# kind of like a comment for a function or a class

def foo():
    """
    this is the foo function
    basically a multi line comment

    the idea is to document the function, it helps you remember what the function should do
    if you've not used it for a while, or helps another person understand your function(s) & class(es)
    """
    pass

##### help()

# you can use help() to read a function docstring: 

# help(foo)       # output below:

# Help on function foo in module __main__:

# foo()
#     this is the foo function
#     basically a multi line comment
    
#     the idea is to document the function, it helps you remember what the function should do
#     if you've not used it for a while, or helps another person understand your function(s) & class(es)

#####

# you can also use it to look at other functions (inbuilt): 

# help(len)

# Help on built-in function len in module builtins:

# len(obj, /)
#     Return the number of items in a container.