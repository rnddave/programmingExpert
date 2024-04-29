# 2023-10-17 - set (data structures) 

###################################

# set = unordered collection of unique objects 

my_set = {1, 2, 3, 4, 5} # remember - unique items... You can put duplicates, but look >>>
print(my_set) # {1, 2, 3, 4, 5}

mySet2 = {1, 1, 2, 3, 4, 4, 4, 5,} # this has duplicates, but look >>>
print(mySet2) # {1, 2, 3, 4, 5}
print(len(mySet2), len(my_set)) # 5 5 (all the duplicates are ignored)

#  you can add things to a set, they are mutable 

# mySet2.add(120,100,50,5, 6, 7, 8, 9, 99) <- this didn't work as can only add 1 argument at a time

mySet2.add(99)
mySet2.add(120)
mySet2.add(100)
mySet2.add(10)
mySet2.add(94)
mySet2.add(7)
mySet2.add(90)
mySet2.add(4)
mySet2.add(5)
mySet2.add(3)
mySet2.add(2)
mySet2.add(1)

# EXPECTED = non-duplicate entries are added
# UNEXPECTED = when printing, they seem to be ordered 

print(mySet2) # {1, 2, 3, 4, 5, 6, 7, 10, 90, 94, 99, 100, 120}

##############
# CHALLENGE TIME >>> 
##############
# array contains [1, 1, 2, 3, 4, 4, 4, 5] 
# and you need to return an array with no duplicates

myArray =  [1, 1, 2, 3, 4, 4, 4, 5] # seed array
# mySet3 = {} <- this didn't work as python assumes we want an empty dictionary
mySet3 = set() # empty set to create space in memory

for i in myArray: # for element in the seed array
    mySet3.add(i) # add the item to the set
    print(mySet3) # should see the set growing

# {1}
# {1}
# {1, 2}
# {1, 2, 3}
# {1, 2, 3, 4}
# {1, 2, 3, 4}
# {1, 2, 3, 4}
# {1, 2, 3, 4, 5}

print(mySet3) # expect a full set, excluding duplicates
# {1, 2, 3, 4, 5}

###################
# ZTM suggested route: 

# OH MY GOD, so simple!!!! 

print(set(myArray)) # {1, 2, 3, 4, 5}
# though this is runtime only
# to save it I guess we could try: 
mySet4 = set(myArray)
print(mySet4) # {1, 2, 3, 4, 5}

######################
# so imagine we want to get rid of duplicates, then we might convert a list to a set (example a website collecting sign-ups, we don't want duplicates)

#######################
#######################
# how about the other way.... 

mySet5 =  {1, 1, 2, 3, 4, 4, 4, 5}

myArray2 = list(mySet5)

print(mySet5, myArray2) # {1, 2, 3, 4, 5} [1, 2, 3, 4, 5]
# creates a list, but only of the unique values

########################

# we cannot access the individual elements in the set? 

#########################################################

# sets have lots of methods, the true value of sets comes from the methods 

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union() 

###############################

mySet6 = {1,2,3,4,5}
yourSet6 = {4,5,6,7,8,9,10}

# sets are very useful when we want to compare them against another

# difference
print(mySet6.difference(yourSet6)) # {1,2,3}
# finds what mySet has that yourSet does not have 
print(yourSet6.difference(mySet6)) # {6, 7, 8, 9, 10}
# original data is not modified

# discard
mySet7 = mySet6.copy() # just creating a copy so I don't lose the original data for these examples 
print(mySet7.discard(5)) # none (because it just discarded it)
print(mySet7,mySet6) # {1, 2, 3, 4} {1, 2, 3, 4, 5}
# original data is modified

# difference_update
mySet8 = mySet6.copy() # just creating a copy so I don't lose the original data for these examples 
print(mySet8.difference_update(yourSet6)) # this will reduce the original set for any values that exist in compared set
print(mySet8)  # {1, 2, 3} 
# original data is modified

# intersection
mySet9 = mySet6.copy() # just creating a copy so I don't lose the original data for these examples 
print(mySet9.intersection(yourSet6)) # {4, 5}
# this one tells us which elements match in both sets 
print(mySet9) # this doesn't change original set = {1, 2, 3, 4, 5}

# isdisjoint()
print(mySet9.isdisjoint(yourSet6)) # False
# this one says (return TRUE if there are no overlaping elements), else FALSE
print(mySet9) # doesn't make any changes to the source set

# issubset()
print(mySet9.issubset(yourSet6)) # False
# these only returens TRUE if all values from one set appear in the other
print(mySet9) # No changes to source data
mySet9b = {4,5}
print(mySet9b.issubset(yourSet6)) # True

# issuperset()
mySet9c = {4,5}
print(yourSet6.issuperset(mySet9c)) # True
# this is the reverse of the issubset() so I have just swapped the arguments around
print(mySet9c) # no change to the source data 

# union()
print(mySet9.union(yourSet6)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# gives us a new set that combines all unique values 
# united these sets together (removing duplicates) 
print(mySet9) # does not change the original set















