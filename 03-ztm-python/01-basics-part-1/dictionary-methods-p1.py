# dictionary methods

user_details = {
    'basket': [1,2,3],
    'greet': 'hello'
}

# print(user_details['age']) # KeyError: 'age'
# but this would kill the program, so we can ask if exists: 

print(user_details.get('age')) # None (but the program continues to run)

# we can also offer a defaul value, in case the key we're looking for does not exist

user_details_2 = {
    'basket': [1,2,3],
    'eyes': 'blue',
    'age': 43,
    'hair': 'brown',
    'weight': False
}

print(user_details_2.get('age', 55), user_details_2.get('weight', 100)) # 43 False

# what I am surprised here is that the weight I provided did not over-write the FALSE value in the dictionary... 

######### ANOTHER WAY TO CREATE A DICTIONARY

# user2 = dict(key=value) for example

user_details_3 = dict(name='david', age=43, eyes='blue')
print(user_details_3) # {'name': 'david', 'age': 43, 'eyes': 'blue'}
# not really a common way to build a dictionary, but is an option




