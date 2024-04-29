# more dictionary methods to note

user_details_2 = {
    'basket': [1,2,3],
    'eyes': 'blue',
    'age': 43,
    'hair': 'brown',
    'weight': False
}


# can we find if something is in a dictionary? YES
print('weight' in user_details_2)   # True

# we can be specific key vs value

print('age' in user_details_2.keys(), 'age' in user_details_2.values()) # True False

######################
# lets look at ITEMS

print(user_details_2.items()) # dict_items([('basket', [1, 2, 3]), ('eyes', 'blue'), ('age', 43), ('hair', 'brown'), ('weight', False)])
# this is a tuple

######################
# we can also copy a dictionary: (we're also going to clear() one to see that we have a populated dictionary and an empty dictionary)

user_details_3 = user_details_2.copy()
print(user_details_2.clear()) # None
print(user_details_3) # {'basket': [1, 2, 3], 'eyes': 'blue', 'age': 43, 'hair': 'brown', 'weight': False}


#######################
# we can use the 'in' command in dictionaries as well

user_details_4 = {
    'basket': [1,2,3],
    'eyes': 'blue',
    'age': 43,
    'hair': 'brown',
    'weight': False
}

print('basket' in user_details_4) # True

####################
# 
# # another dictionary method 'keys'

print('age' in user_details_4.keys()) # True

# and values

print('brown' in user_details_4.values()) # True

# but we can also look at the whole row - item

print(43 in user_details_4.items()) # False ??? 
# not sure why this is false... 
print('age' in user_details_4.items()) # False ???

##############################
# we can look at all the items

print(user_details_4.items())
# dict_items([('basket', [1, 2, 3]), ('eyes', 'blue'), ('age', 43), ('hair', 'brown'), ('weight', False)])
# this is a tuple

##########################
# can inplace remove dictionary items:

user_details_4.clear()
print(user_details_4) #{}

##########################
user_details_5 = {
    'basket': [1,2,3],
    'eyes': 'blue',
    'age': 43,
    'hair': 'brown',
    'weight': False
}

# interestingly, we can copy a dictionary, so we have a clone, but then clear the original
# this gives us a populated dictionary and an empty dictionary 
# (they are unique objects, not the same object with different pointres)

user_details_6 = user_details_5.copy()
print(user_details_6, user_details_5)

#   create the copy 
#   {'basket': [1, 2, 3], 'eyes': 'blue', 'age': 43, 'hair': 'brown', 'weight': False} {'basket': [1, 2, 3], 'eyes': 'blue', 'age': 43, 'hair': 'brown', 'weight': False}
#   clear the original

user_details_5.clear()

print(user_details_5, user_details_6)
# {} {'basket': [1, 2, 3], 'eyes': 'blue', 'age': 43, 'hair': 'brown', 'weight': False}

##########
# we can remove items:

user_details_7 = {
    'basket': [1,2,3],
    'eyes': 'blue',
    'age': 43,
    'hair': 'brown',
    'weight': False
}

user_details_7.pop('basket')

print(user_details_7) # {'eyes': 'blue', 'age': 43, 'hair': 'brown', 'weight': False}

##############
# popitem()
# pops the last item from the dictionary, regardless of what it is
# interestingly, this used to drop something at random, completely random, 
# but that was changed in Python 3.7 to drop last Key:Value pair instead 
# the new (pop last pair) approach is probably more useful tbh as a lot more predictable

user_details_8 = {
    'basket': [1,2,3],
    'eyes': 'blue',
    'age': 43,
    'hair': 'brown',
    'weight': False
}

user_details_8.popitem()

print(user_details_8)
# {'basket': [1, 2, 3], 'eyes': 'blue', 'age': 43, 'hair': 'brown'} 

##############################################

# we can update a key:value using update()

user_details_9 = {
    'basket': [1,2,3],
    'eyes': 'blue',
    'age': 43,
    'hair': 'brown',
    'weight': False
}

print(user_details_9.update({'hair': 'brownish'})) # outputs a None for some reason...
print(user_details_9) # {'basket': [1, 2, 3], 'eyes': 'blue', 'age': 43, 'hair': 'brownish', 'weight': False}

# ABOVE we are updating the existing key:value 
# but if the key doesn't exist, then it will add it
# below we add one... 

print(user_details_9.update({'fav color': 'black'})) # None

print(user_details_9) # {'basket': [1, 2, 3], 'eyes': 'blue', 'age': 43, 'hair': 'brownish', 'weight': False, 'fav color': 'black'}




