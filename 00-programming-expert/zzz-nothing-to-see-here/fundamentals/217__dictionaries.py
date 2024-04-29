## dictionary in python (dict) is a collection that associates immutable keys with values of any type

x = {"Brad": 10,
    "Lucy": 12,
    "John": 6.5,
}
## allows us to hold key value pairs
# "Brad" the key, 10 = the key value

## Salary example:: 

salaries = {
    "Brad": 10,
    "Lucy": 12,
    "John": 6.5,
}

# how to add items to a dictionary
salaries["david"] = 21

# now lets look at content from the dict
for name in salaries:
    salary = salaries[name]
    print(f"{name} makes ${salary} an hour")


for name, salary in salaries.items():
    weekly_salary = salary * 40
    print(f"{name} makes ${weekly_salary} an week")

######################################

## going back to the X dict example 

# to del a key
del x["Brad"]
print(x)

# how to add items to a dictionary
x["Brad"] = 10
print(x)

## does a key exist in dict?
contains = "Lucy" in x
print(contains)

## but what if you want to know if the key value exists rather than the key? 
values = x.values() #this actually gives us the values in what looks like a list: 
print(values)
# output looks like >> dict_values([12, 6.5, 10])
keys = x.keys()
print(keys)

## now to look at the items
items = x.items() #this one looks like tuples
print(items)
print(len(x)) # this gives you the number of key:value pairs

## what if we want to loop through a dictionary? 
## a dictionary is an unordered collection of items, so we do not know which order things will appear
## therefore we cannot use index to find items
## we'd need to loop through all of the keys in the dictionary to be able to then access the value
for key in x:
    value = x[key]
    print(key, value)
# alternatively: 
for key, value in x.items():
    print(key, value)

## the .get method

y = {2: 1, 3: 3}
y[4] = y.get(4, 0) + 1 # this allows us to get the key 4, but if it doesn't exist, it will add the value 1 for new key 4:
print(y) # output = {2: 1, 3: 3, 4: 1}

#### but why use a dictionary ####
# one of most common uses of dict is to keep track of characters etc, the frequency of use etc 

chars = {}
string = "hello world"

for char in string:
    chars[char] = chars.get(char, 0) + 1 #create a new key, or if exists, increase the value
print(chars) # output = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

## another example

counts = {}

while True:
    num = input("Number (enter q to quit): ")

    if num == "q":
        break

    num = int(num)
    counts[num] = counts.get(num, 0) + 1

print(counts)

## when to use a dictionary
# when you can store data in an unordered state
# using a dictionary is a very quick way of finding data 
# quicker than searching through a list for example

d = {"a": 1, "b": 2, "c": 3, "d": 4}
l = ["a", "b", "c", "d"]

# with a list, you have to look at each item iteratively. In this case, the list is small, 
# but if you had millions of items, it could be quite time expensive
# whereas with the dictionary, to find if "d" exists, this is almost an instant return. 

### Practice 217.03
# what does this output?

#  words = {"is": 2, "hello": 3, "the": 4}
#  this_count = words["this"]
#  print(this_count) # answer = an exception, you cannot access a key that doesn't exist

### Practice 217.04
# white a prog that asks user to input a string and then presents how much each character appears 

chars = {}
string = input("Enter a string: ")

for char in string:
    chars[char] = chars.get(char, 0) + 1 #create a new key, or if exists, increase the value

for key, value in chars.items():
    print(f"{key}: {value}") 

## the above worked almost on first try :D 
## an alternative: 

string = input("Enter a string: ")

character_frequencies = {}

for character in string:
    if character not in character_frequencies:
        character_frequencies[character] = 0

    character_frequencies[character] += 1

for key in character_frequencies:
    frequency = character_frequencies[key]

    print(f"{key}: {frequency}")