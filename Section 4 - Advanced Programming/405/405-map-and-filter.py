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
# practice >> 405.05 - 
###################################
