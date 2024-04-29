# for lopps 

for item in 'One More David':
    print(item)
"""     
O
n
e
 
M
o
r
e
 
D
a
v
i
d
"""
# ^^ this is basically a multiline comment - not really a thing in python but this works

for item in 'One More David':
    for x in [1,2]:
        print(item * x)

"""
O
OO
n
nn
e
ee
 
  
M
MM
o
oo
r
rr
e
ee
 
  
D
DD
a
aa
v
vv
i
ii
d
dd
"""

######################################

# MORE ON ITERABLES
# an object or collection that can be iterated over 

"""
list
string
set
tuple
dictionary 
"""

print('\n') #just adding some white space here
print('\n') #just adding some white space here

# dictionary has a little bit of a different consideration 

user = {
    'name': 'DD',
    'age': 99,
    'blueEyes': False
}

for item in user:
    print(item)
"""
name
age
blueEyes
"""
# so we have the keys, not the values! 

# dictionaries have 3 methods that are useful when iterating 
# items
# values
# keys

for item in user.items():   # (key:value pairs)
    print(item)
"""
('name', 'DD')
('age', 99)
('blueEyes', False)
"""

for item in user.values():  # the values
    print(item)
"""
DD
99
False
"""

for item in user.keys():  # the keys
    print(item)
"""
name
age
blueEyes
"""

###############################
print('\n') #just adding some white space here
print('\n') #just adding some white space here

# coming back to this example

for item in user.items():   # (key:value pairs)
    print(item)
"""
('name', 'DD')
('age', 99)
('blueEyes', False)
"""
# we're actually getting tuples, which we can unpack like so: 
print('\n') #just adding some white space here
print('\n') #just adding some white space here


for item in user.items():   # (key:value pairs)
    key, value = item
    print(key, value)
"""
name DD
age 99
blueEyes False
"""

# we can clean this up: 

for key, value in user.items():     # some times seen as for 'k, v' in user.......
    print(key, value)
"""
name DD
age 99
blueEyes False
"""

###############################
print('\n') #just adding some white space here
print('\n') #just adding some white space here

# some fun
# use a loop to sum up the contents of a list: 

myList = [1,2,3,4,5,6,7,8,9,10]
theAnswer = 0

for item in myList:
    theAnswer = theAnswer + item

print(theAnswer)    # 55










