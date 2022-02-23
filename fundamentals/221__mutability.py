## immutable object = object that cannot be changed once created: 
# int, float, str, bool, tuple

## mutable object = something that can be changed after creation 
# list, set, dict

x = [1, 2, 3, 4]
y = x                   # this is not a copy of x, it's like a symlink to the original object
y.append(5)

print(x)
print(y)
print(x is y)

y = x[:]               # this is a copy of the original object
print(x is y)
print(x == y)

########################
print("\n \n \n \n")
########################
a = 1
b = a                   # this is not a copy of a, it's like a symlink to the original object
print(a is b)

a += 1
print(a is b)

## id() - memory address location? 
a = 1
b = a
print(a is b)           # objects are the same
print(id(a), id(b))     # 4416571696 4416571696 = the same memory address
a += 1                  # changing one of the objects
print(a is b)           # False = objects no longer the same
print(id(a), id(b))     # 4518406480 4518406448 note the memory locations are now different 45184064[80] 45184064[48]

####################
# examples; mutable, immutable

x = (1, 2, 3)           # immutable, therfore we cannot change a tuple, we need to define a new one instead
y = (1, 2, 4)           # tuples are an interesting data type

####### list

x = []

def func (lst, x):
    lst.append(x)       # because a list is mutable, we can modify it in place
    print(lst, id(lst))

a = []
func(a, 2)
func(a, 3)
print(a, id(a))

####### dictionary

d = {}
d["k"] = "v"

a = d
a["a"] = "b"

print(d, id(d), "\n", a, id(a))
print( d is a)

####### set

s1 = set()
s2 = s1

s1.add(1)
s2.add(2)

print(s1, s2)

def func(s, x):
    s.add(x)

s1 = set()
func(s1, 1)
print(s1)

################# COPIES

# what if you want to make a copy of the object, but have a new object rather than modifying an existing mutable object

### COPY LIST 

a = [1, 2, 3]
b = a[:]        # slice, and with a single colon, equal start at end and go to begining

print(a is b, id(a), id(b))     # False 4516953280 4516952128

###

def func(lst):
    lst = lst[:]    # this makes a copy of the lst (using slice), it does have same name, but it is a copy not the original list
    lst.append(4)   # adding 4 to our NEW list
    print(lst)      # [1, 2, 3, 4]

x = [1, 2, 3]
func(x)
print(x)            # [1, 2, 3]

### COPY SET

s1 = {1, 2, 3}
s2 = s1.copy()      # this creates what is called a SHALLOW COPY

s1.add(4)
print(s1, s2)       # {1, 2, 3, 4} {1, 2, 3} (s2 is a copy of s1, before s1.add(4) took place, which is why they look different)

### COPY Dictionary

s1 = {"k": "v"}
s2 = s1.copy()      # this creates what is called a SHALLOW COPY

s1[1] = 2
print(s1, s2)       # {'k': 'v', 1: 2} {'k': 'v'}

##############    NESTED MUTABLE DATA TYPES    ##############

##############    NESTED LISTS    ##############

lst = [[1, 2, 3], [3, 4, 5]]    # this is 2x mutable objects within another mutable object [nested lists]
lst[0].append(4)
lst[1].append(9)
print(lst)          # [[1, 2, 3, 4], [3, 4, 5, 9]]

lst[0].clear()
print(lst)          # [[], [3, 4, 5, 9]]
lst[1].clear()
print(lst)          # [[], []]
lst.clear()
print(lst)          # []

##############    NESTED Dictionaries    ##############

lst = [1, 2, 3]
d = {1: lst}        # this dictionary is made up of key 1 + lst (as the value) 

lst.append(4)       # we're now adding 4 to the lst ( a new value)
print(d)            # {1: [1, 2, 3, 4]}  -- this tells us that the key 1 in dictionary has the values of list (including the append)

##############    storing mutable objects that are inside an immutable object    ##############

a = [1, 2]              # the list is mutable
b = [3, 4]

tup = (a, b)            # the tuple is immutable (cannot be changed), BUT is made of mutable objects

print(tup, type(tup))   # ([1, 2], [3, 4]) <class 'tuple'>

a.append(1)
print(a, b, tup)        # [1, 2, 1] [3, 4] ([1, 2, 1], [3, 4])

##############    Shallow vs Deep copies   ##############

a = [[1, 2 ,3]]
b = a[:]            # slice, a copy
print(a, b)         # [[1, 2, 3]] [[1, 2, 3]]
print(a is b)       # False

c = a[0]            # c is a symlink of a, index 0
print(c)            # [1, 2, 3]

c.append(4)         # c is a copy of index[0] in a === so add the 4 to index 0
print(a, b, c)      # [[1, 2, 3, 4]] [[1, 2, 3, 4]] [1, 2, 3, 4]

a.append(1)         # there is no index, so this will be the next item in the list, index 1 (also, value 1 in this case)
print(a, b, c)      # [[1, 2, 3, 4], 1] [[1, 2, 3, 4]] [1, 2, 3, 4] 

# a shallow copy, copies the object, but not everything inside the object
# a deep copy copies the object and what is in the object, it is not common to need a deep copy
# deep copies were not covered in this course. 

##############    Practice  ##############

## 221.04 -- take 3 parameters [list], [target] and [swap_value]
############ replace instances of [target] in [lst] with [swap_value]
############ don't return anything

def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        element = lst[idx]

        if element == target:
            lst[idx] = swap_value


lst = ["tim", "is", "great"]
target = "is"
swap_value = "hello"
replace(lst, target, swap_value)
print(lst)


##### below is some test code that is on the page, I am unsure what it does as does not compile for me
# import unittest

# import program

# class TestProgram(unittest.TestCase):
#     def test_case_1(self):
#         lst = []
#         target = ""
#         swap_value = ""
#         program.replace(lst, target, swap_value)
#         self.assertEqual([], lst)

#     def test_case_2(self):
#         lst = ["tim", "is", "great"]
#         target = "is"
#         swap_value = "hello"
#         program.replace(lst, target, swap_value)
#         self.assertEqual(["tim", "hello", "great"], lst)

#     def test_case_3(self):
#         lst = ["tim", "is", "great"]
#         target = "world"
#         swap_value = "hello"
#         program.replace(lst, target, swap_value)
#         self.assertEqual(["tim", "is", "great"], lst)

#     def test_case_4(self):
#         lst = ["a", "b", "c"]
#         target = "a"
#         swap_value = "d"
#         program.replace(lst, target, swap_value)
#         self.assertEqual(["d", "b", "c"], lst)

#     def test_case_5(self):
#         lst = ["tim", "is", "great", "tim", "is", "tim"]
#         target = "tim"
#         swap_value = "world"
#         program.replace(lst, target, swap_value)
#         self.assertEqual(["world", "is", "great", "world", "is", "world"], lst)

#     def test_case_6(self):
#         lst = ["tim", "is", "great", "tim", "is", "tim"]
#         target = "tim"
#         swap_value = "tim"
#         program.replace(lst, target, swap_value)
#         self.assertEqual(["tim", "is", "great", "tim", "is", "tim"], lst)

#     def test_case_6(self):
#         lst = ["i", "love", "programmingexpert"]
#         target = "programmingexpert"
#         swap_value = "algoexpert"
#         program.replace(lst, target, swap_value)
#         self.assertEqual(["i", "love", "algoexpert"], lst)