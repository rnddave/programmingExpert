#### LIST UNPACKING ####

newBasket17 = [1, 3, 5, 7, 9]

# what if we want to target items: 

a,b,c = [1,2,3]

print(c, a, b) # 3 1 2

# but we can build on this... maybe we want some values and the remainder as a list

a, b, c, *donkey = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(c, a, donkey, b) # 3 1 [4, 5, 6, 7, 8, 9] 2

# interestingly, if we declare other values, they will take items from the list as well: 

a, b, c, *donkey, d, e = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a, b, c, donkey, d, e) # 1 2 3 [4, 5, 6, 7] 8 9

# we can obviously pull just some values: 

print(d, type(d)) # 8 <class 'int'>







