# 2023-10-17 - Tuples  
# first save to generate new file

# Tuples are like lists, but cannot be modified (immutable lists) 

myTuple = (1,2,3,4,5)

print(myTuple[2]) # 3
print(5 in myTuple) # True

# Benefits = you always know what's in the tuple
# usually faster than lists

# BUT - cannot modify, so less flexible 

####################

new_tuple = myTuple[1:2]

print(new_tuple) #(2,) <- why the comma - because it's a tuple, it has the , on the end (?)

new_tuple2 = myTuple[1:4]
print(new_tuple2) # (2, 3, 4) - why this one doesn't have a comma - I don't know

#############

# Methods we might care about

##### count() & index()

new_tuple3 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5,5,5,5,5,)

# count() 
print(new_tuple3.count(5)) # 7

# index() 
print(new_tuple3.index(5)) # 4 (this is the first instance of)

#################
# but can also use things like lenght

print(len(new_tuple3)) # 19







