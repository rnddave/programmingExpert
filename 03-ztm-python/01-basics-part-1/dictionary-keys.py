# dictionary keys

# a dictionary key can be: 
# char, string, int, boolean

# dictionary keys need to be immutable (cannot change) so a key can't be a list for example (which can be changed)
# a key does need to be unique though, so no duplicates

dictionary = {
    '123': [1,2,3],
    '123': 'hello'
}

print(dictionary)   # {'123': 'hello'}
print(dictionary['123'])    # hello

# what we can see is that although we have multiple entries, they are using the same key, therefore the second key over-writes the first key
