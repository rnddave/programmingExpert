### math functions & features built into python, saving you some time later

# abs()         # absolute value, value that is possible
x = abs(-9)
print(x)        # 9 == removed the '-'
x = abs(9)
print(x)        # 9 == the absolute of a positive number = the positive number

# max()         # find the maximum
x = max(2, 3)
print(x)        # 3 

y = max([1, 2, 5])
print(y)        # 5

z = max("a", "b", "A", "B")
print(z)        # b     === lowercase letters have higher ASCII value than uppercase letters

# min()         # find the minimum
x = min(2, 3)
print(x)        # 2 

y = min([1, 2, 5])
print(y)        # 1

z = min("a", "b", "A", "B")
print(z)        # A     === lowercase letters have higher ASCII value than uppercase letters

# sum()
x = sum([1, 2, 3])
print(x)        # 6

# round()               # round to some digits
x = round(3.45)
print(x)                # 3
x = round(3.459)        
print(x)                # 3
x = round(3.4555, 2)
print(x)                # 3.46
x = round(3.45, 1)
print(x)                # 3.5

####    MATH MODULE    ####

import math

x = math.sin(90)        # these trig functions are working with radions, not degrees 
print(x)

####    RANDOM MODULE    ####

import random

random_num = random.randint(1, 200)         # in the range 1 - 200 (start, stop)
print(random_num)

random_num = random.randrange(1, 200, 2)    # start, stop, step (i.e. only consider odd numbers)
print(random_num)

lst = ["he", "hi", "ho", "hum", "hello"]
word = random.choice(lst)
print(word)

#################

import math

a = 41
b = 42

print("Max of a and b:", max(a, b))
print("Min of a and b:", min(a, b))

print("Max of 1, 2, 3, 4:", max([1, 2, 3, 4]))
print("Min of 1, 2, 3, 4:", min([1, 2, 3, 4]))

print("Sum of -1, -2, -3, 4:", sum([-1, -2, -3, 4]))

print("3.14 rounded to the nearest integer:", round(3.14))
print("2.78 rounded to the nearest integer:", round(2.78))

print("Absolute value of -10:", abs(-10))

print("Highly precise value of pi:", math.pi)