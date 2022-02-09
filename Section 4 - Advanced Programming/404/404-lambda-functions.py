"""
Lambda Functions

- an anonymous function
- can be defined in-line 
-- without the use of the [def] keyword

this can be useful when defining custom sort order for a collection as an example
"""

add_one = lambda x: x + 1

print(add_one(1))
print(add_one(41))

"""
2
42
"""

# hyphenise = lambda s: (this is basically calling the function), what comes after the : = the function code
hyphenise = lambda s: s.lower().replace(" ", "-")
print(hyphenise("Hello World"))

# hello-world

# -=-= =- =-=- =-= -=-= =- =-=-

func = lambda x, y, z=0: x + y + z

print(func(1, 2))               # 3
print(func(3, 5, 7))            # 15

# = = = = = = = = = = = = = = = =

lst = [(1, 6), (-2, 4), (3, 4)]
lst.sort(key=lambda x: x[1])
print(lst)                      # [(-2, 4), (3, 4), (1, 6)]

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

mul = lambda x: lambda y: x * y
result = mul(2)
print(result)                   # <function <lambda>.<locals>.<lambda> at 0x10b5a34c0>

# so we need to change it to pass another value as well

print(result(4))                # 8 (2x4)

# wtf - this bit is 'abstract' !!

###################################
# practice >> 404/05 - lambda Function
###################################

"""
write a lambda function(s)

- take 3 integer or float parameters and return their sum
-- variable called [add_variable]

- take 2 string parameter 
- return maximum of their lengths
-- [max_length]

- take 2 list parameters
- return a set containing elements from both lists
-- [create_set]
"""

# solution 1

add_values = lambda x, y, z : x + y + z

max_length = lambda x, y: max(len(x), len(y))

create_set = lambda x, y: set(x).union(y)

# solution 2

add_values = lambda x, y, z : sum([x, y, z])

max_length = lambda x, y: max(len(x), len(y))

create_set = lambda x, y: set(x + y)

# solution 3

add_values = lambda x, y, z : sum([x, y, z])

max_length = lambda x, y: max(len(x), len(y))

create_set = lambda x, y: set(x) | set(y)