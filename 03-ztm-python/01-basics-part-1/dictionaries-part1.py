#### dictionaries

# other languages may use the term - Map, object, hash-table, etc

# data types and data structures! 

my1stDict = {
    'a': 1,
    'b': 3,
    'c': 5
} # these are key-value pairs

print(my1stDict['b']) # 3

# a dictionary is all over the place, all over memory. Not nec. in order

# we can access any element in a dictionary

mySecondDict = {
    'a': [1,2,3,4],
    'b': 'hellllllloooooo',
    'c': 69
}

print(mySecondDict)
print(mySecondDict['a'])
print(mySecondDict['a'][2])
# {'a': [1, 2, 3, 4], 'b': 'hellllllloooooo', 'c': 69}
# [1, 2, 3, 4]
# 3 

#-------------

print('---------------------------------------------')

#-------------

my_list = [
    {
        'a': [1,2,3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4,5,6],
        'b': 'hello',
        'x': True
    }
]

print(my_list[0]['a'][2])
print(mySecondDict['a'][1])

# when to use...

# dictionary had no order
# a list has order

# dictionaries hold more information than a list (a list can hold a dictionary, but deep down, it is just an index)
# vs a dictionary that has a key and a value. 


