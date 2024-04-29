# == vs is

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# True
# False
# False
# True
# True

# logical operators - hopefully used with comparing two of the same data types
# python will do some changing for you but you shouldn't really rely on it

print('1' == 1) # also false, didn't do type conversion
print('\n') #just adding some white space here

# --------------------
# now what does this look like with IS

print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])

#False
#False
#False
#False
#False  (different memory location)

# IS actually checks location in memory to see if it is the same

print('\n') #just adding some white space here
print(True is True)     # true = because they are the same location
print(1 is 1)           # true = the same memory location
print([] is [])         # false = these are in different locations in memory

# -------------------

# IS = stricter than == (equality)

