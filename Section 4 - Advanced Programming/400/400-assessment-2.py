###################################
# 400.02- INTEGER SUM
###################################

"""
write a function called [integer_sum]
- accept any number of positional arguments (assumed to be integers)
- function to return the sum of all these integers

HOWEVER - error handling >>> 
- write following decorators
-- [flatten_lists] = flatten any [list] arguments
--- extract elements, pass them as individual arguments instead of a list
--- remove any non-integer components of the list

-- [convert_string_to_ints]
--- convert any string arguments that are valid integers to integers
--- pass them to the decorated function
--- remove any non-integer components from the string

-- [filter_integers]
--- decorator should remove any argument that iis not an integer
--- then call the decorated function with only integer arguments
"""

def flatten_lists(func):
    def wrapper(*args):
        new_args = []                           # new empty list

        for arg in args:                        # for each argument passed
            if isinstance(arg, list):           # is the argument peing passed a list?
                new_args.extend(arg)            # if the arg is a list, then add each item of old list to new list
            else:
                new_args.append(arg)            # if argument is just a single integer, then just add that single item to list

        result = func(*new_args)                # return some *new_args
        return result                           # pass it to the wrapper

    return wrapper                              # pass it to the function

def convert_strings_to_ints(func):
    def wrapper(*args):
        new_args = []                           # new empty list

        for arg in args.split():                # split components of a string
            try:
                new_args.append(arg)            # add the item to the end of the new_list item
            except ValueError:
                pass

        result = func(*new_args)                
        return result                           # return the result
    
    return wrapper


def filter_integers(func):
    def wrapper(*args):
        new_args = []                           # new empty list

        for arg in args:                        # for each argument passed
            if isinstance(arg, int):            # is the argument peing passed a int?
                new_args.append(arg)            # if the arg is a int, then add item to new list
 
        result = func(*new_args)                # return some *new_args
        return result                           # pass it to the wrapper

    return wrapper                              # pass it to the function

@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)

"""
try it - FAILED EVERY TEST

"""