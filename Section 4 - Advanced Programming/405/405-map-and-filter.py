"""
Map and Filter

two nifty functions that will help you deal with iterable objects in manu situations
"""

lst = [i for i in range(10)]
plus_two = map(lambda x: x + 2, lst)
evens = filter(lambda x: x % 2 == 0, lst)
odds = filter(lambda x: x % 2 == 1, lst)

print("Original List:", lst)
print("Plus 2:", list(plus_two))
print("Evens:", list(evens))
print("Odds:", list(odds))

"""
Original List: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Plus 2: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Evens: [0, 2, 4, 6, 8]
Odds: [1, 3, 5, 7, 9]
"""

lst = [i for i in range(50)]
new_lst = list(map(lambda x: x**2, lst))
print(new_lst)

# another example, suppose a list of lists and we want to know the sum of each sub-list

lst2 = [[1, 2, 3, 4], [3,4,5,6], [5,6,7,8,8]]

new_lst2 = list(map(lambda x: sum(x), lst2))
print(new_lst2)                                     # [10, 18, 34]

# filters

lst3 = [[1, 2, 1, 1], [3,4,5,6], [5,6,7,8,8]]
new_lst3 = list(filter(lambda x: sum(x) > 6, lst3)) # filter lets you take results where conditions are true
                                                    # in this case I want to find list(sub-list)
                                                    # that contain a sum greater than 6, ese discard
print(new_lst3)                                     # [[3, 4, 5, 6], [5, 6, 7, 8, 8]]


"""
map and filters together!! 
"""

lst4 = [[1, 2, 1, 1], [3,4,5,6], [5,6,5,5,5,5,5,7,8,8]]

new_lst4 = filter(lambda y: y% 2 == 0, map(lambda x: sum(x), lst4))
print(list(new_lst4))                               # [18]


###################################
# practice >> 405.01 - what is the output
###################################

lst = ["algoexpert", "is", "the", "best"]
x = map(len, lst)
print(list(x))

"""
my guess is 4, I thought number of list items

misread question, answer is [10, 2, 3, 4]

as in length of each list item AND in list form
"""

###################################
# practice >> 405.02 - what is the output
###################################

lst = [[2, 3, 4], [4, 5, 6], [1, 1, 1], [0, 0], [-5, -7]]
x = filter(lambda a: abs(sum(a)) > 10, lst)
print(list(x))

"""
my guess: 

[[15], [-12]]

nope!! 

the actual output was to return the list items that would sum up greater than 10

[[4, 5, 6], [-5, -7]]

"""

###################################
# practice >> 405.03 - map and filter
###################################

"""
use [map] and [filter] functions to create an iterable that contains the even squares of all elements in the [lst] list.

once created, this iterable print out all values on own line

ensure you use lambda of course
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square the list, using map function 
squares = list(map(lambda x: x ** 2, lst))

# now we want to find the result of squares that are even, using filter
evens = filter(lambda y: y % 2 == 0, squares)

# following line provided me with a list, but we need to see each on own line
# print(list(evens))

# I will revert to code from 403, where we used a for loop to extract each item from the list on own line
for val in evens:
    print(val)


###################################
# 405.03 - solution 1
###################################

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = map(lambda x: x ** 2, lst)
even_squares = filter(lambda x: x % 2 == 0, squares)

for value in even_squares:
    print(value)

###################################
# 405.03 - solution 2 (I really like this one)
###################################

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, lst))

for value in even_squares:
    print(value)