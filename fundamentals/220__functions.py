def add_numbers(a, b):
    return a + b


def print_stars(n):
    for i in range(n + 1):
        print(i * "*")

    for i in range(n, -1, -1):
        print(i * "*")


print_stars(add_numbers(4, 3))

## functions

# def print_value(value): # need to use def to define the function
#     print(value)        # obviously, useless, but the basic structure is here

# def print_value           # function name
# def print_value()         # parameters of the function (using whatever is passed when it is called) (no parameters is also okay)
#    print("hello")         # what we want to return 

# when you call a function () any arguments you add to the () will be passed to your function as a parameter 

def add_5(x, y):
    result = x + y + 5
    print(result)

x = 4
y = 5

add_5(x, y)

## using the return keyword

def add_5(x, y):
    result = x + y + 5
    return result

x = 3
y = 54

r = add_5(x, y)
print(r)

## using the return keyword, multiple returns

def add_5(x, y):
    result = x + y + 5
    if result < 0:
        return result

    return 1

x = 3
y = -9

r = add_5(x, y)
print(r)

## using default values
# default allows the function to operate with an argument being passed, or no argument being passed
# if no argument passed, then use default parameter 

def new_range(start=0, stop=10): # (the =0, =10 == the default parameters)
    x = start

    while x < stop:
        print(x)
        x += 1

new_range(1, 8)         # with arguments passed
new_range()             # no argument = use defaults
new_range(stop=5)       # just passing the stop argument

## returning multiple values from our functions 

def return_values(x, y):
    return x + 1, y + 1

result = return_values(1, 2)
print(type(result), result)

############################
# practice

def remove_chars(string1, string2=""):      # if no chars passed to string 2, then no changes occur to string 1
    new_string = string1
    for char in string2:
        new_string = new_string.replace(char, "")

    return new_string

result = remove_chars("hello World", "l")   # the second argument = l, this will pass to function and then remove l from our string
print(result)                               # output = heo Word

##########

def sum_list(list1, list2):
    list1_sum = sum_list(list1)
    list2_sum = sum_list(list2)
    return list1_sum, list2_sum

def sum_list(lst):
    total = 0

    for num in lst: 
        total += num

    return total

sum1, sum2 = sum_list([1, 2, 3, 4], [-1, -2, -3, -4])   # this is not working at time of writing!
print(sum1, sum2)