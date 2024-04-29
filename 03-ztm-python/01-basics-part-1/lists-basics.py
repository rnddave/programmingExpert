myFirstList = [1, 2, 4, 6, 8, 9, 'a', 'dog', 'bigger']

print(myFirstList[0::2]) # [1, 4, 8, 'a', 'bigger']

# this is list slicing, basically the same as with strings. 

print(myFirstList[::-1]) # ['bigger', 'dog', 'a', 9, 8, 6, 4, 2, 1]

# good news - lists are muttable (we can change things)

myFirstList[6] = 'mouse'
print(myFirstList) # [1, 2, 4, 6, 8, 9, 'mouse', 'dog', 'bigger']

mySecondList = myFirstList 
# this is tricky in python, it's just a reference to the same memory location, so changes in one affect the other

mySecondList[2] = 'boo'
print(myFirstList, mySecondList) 
# [1, 2, 'boo', 6, 8, 9, 'mouse', 'dog', 'bigger'] 
# [1, 2, 'boo', 6, 8, 9, 'mouse', 'dog', 'bigger']

myThirdList = myFirstList[:] # this should make a complete independant copy (not a reference)

myThirdList[2] = 'SCARY'

print(myFirstList, myThirdList)
# [1, 2, 'boo', 6, 8, 9, 'mouse', 'dog', 'bigger'] 
# [1, 2, 'SCARY', 6, 8, 9, 'mouse', 'dog', 'bigger']

########################
# MULTI DIMENSIONAL LIST = MATRIX
# A list with a list inside it

myMatrix = [
    [1,2,3],
    [2,3,4],
    [3,4,5],
    [4,5,6],
    [1,[2,3,4]]
]

print(myMatrix)
print(len(myMatrix))

########################
# append

basket2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(basket2)
newBasket = basket2.append(10) # this changes the list in place (adds to end of existing list)

print(newBasket) # None = WHY = NOT SURE
print(basket2)

# if we wanted to create a new list that had that extra item, we'd need to do it like so: 

basket2.append(11) # will add 11 to the end of the list
newBasket = basket2 # this is now a new list that copies the list with the 11 on it
print(newBasket)

newBasket.pop(-2) # will delete the second from last item
print(newBasket) # 1-9, 11

newBasket.pop() # will just remove the last one

# we can also remove by value (not by index)
# see below (AFTER EXTENDS)

newBasket.insert(3, 12) # this says, at the 3rd index, insert number 12
print(newBasket) # [1, 2, 3, 12, 4, 5, 6, 7, 8, 9, 11]

### if we want to add multiple items

basket3 = newBasket
basket3.extend([13, 14, 15, 16])
print(basket3) # [1, 2, 3, 12, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16]

basket3.remove(12) # THIS WILL REMOVE by VALUE, NOT by index - so will remove value 12 in this case
print(basket3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16]










