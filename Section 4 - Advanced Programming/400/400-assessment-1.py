###################################
# 400.01 - Positive Even Squares
###################################

"""
Write a function that accepts any number of positional arguments, all of which you may assume will be lists of integers

Your function should filter all of these lists such that they only contain even positive integers 
- and combine all of the lists into one list of integers

Your function should then modify the combined list such that is contains the squares of all the elements and return the list

Use a cobination of the map, filter, lambda functions/keywords to modify the lists

"""

# STEPS > function to accept any number of positional arguments (lists of integers)
# STEPS > remove the odd numbers from each [list(n)], passing to a [new_list] containing only even numbers (MAP/FILTER?)
# STEPS > modify [new_list] so that it contains and returns the squared sum of [new_list] (possibly in another list? [return_list]) (LAMBDA)


def positive_even_squares(*args):
    even_numbers_only = []

    for item in args:
        only_pass_the_evens = filter(lambda x: x > 0 and x % 2 == 0, item)
        even_numbers_only.extend(only_pass_the_evens)
         
    
    squares_lst = map(lambda x: x ** 2, even_numbers_only)

    return list(squares_lst)


try1 = positive_even_squares([1, 2, 3, 4])
try2 = positive_even_squares([2, 5, 7, 2])

print(try1)
print(try2)