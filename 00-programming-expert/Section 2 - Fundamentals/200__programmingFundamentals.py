print('hello world')

print("type of 3", type(3))

print('type of "Hello"', type("Hello"))

print("type of True", type(True))

# 2.04 variables & printing 

a = 1
b = "hello"
c = True

print(a, b, c)

# 2.05 input

name = input("What is your name? ")

print("Hello,", name)

name2 = input("What is your name? ")

print("Hello, " + name2)

# 2.07 type conversions

d = "42"
e = int(d)

print(d, type(d))
print(e, type(e))

str_number = input("Type a number: ")
int_number = int(str_number)

result = int_number + 5

print(result)

# 2.08 conditions

a = 1
b = 2
c = 3

print(a == 1)
print(a == 2)
print(a + b == c)

print(a - b > c)
print(a ** b < c)

# test your self - 2.08

w = 1
x = 1
y = 3
z = 2

condition_1 = w < x + y
condition_2 = x == y - 2
condition_3 = z != 0
condition_4 = z + z == z * z
condition_5 = w > 0

print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)
print(condition_5)

# test 2 - 2.08

w = "c"
x = "hello"
y = "hello"
z = "j"

condition_1 = w != "a"
condition_2 = w < x
condition_3 = x == y
condition_4 = y == "hello"
condition_5 = z > "c"

print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)
print(condition_5)

# 2.09 Compound Conditions

a = 1
b = 2

print(a == 1)
print(not(b == 3))
print(a == 1 and b == 3)
print(a == 1 or b == 3)
print(a == 1 and b == 2)
print(a == 1 and b == 3)
print(a == 1 or b == 2)

# test yourself - 2.09 

w = True
x = True
y = False
z = True

condition_1 = w and x and not y or not z
condition_2 = not (w and not w)
condition_3 = not (w and y or y)
condition_4 = x and (y or z and w)

print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)

