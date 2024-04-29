"""
Generators

special kind of iterator that uses the [yeild] keyword to return the next value in a sequence
"""

# I bet you couldn't store all of those in a list! There are an
# infinite number of even numbers but generators solve this problem
# easily!
from pkg_resources import yield_lines


def all_even_numbers():
    i = 0
    while True:
        if i % 2 == 0:
            yield i
        i += 1


count = 0
for even_number in all_even_numbers():
    print("Even number:", even_number)
    count += 1

    # Let's just print 10 even numbers, but this could run forever
    # if we wanted to let it!
    if count >= 10:
        break

"""
OUTPUT >>>

Even number: 0
Even number: 2
Even number: 4
Even number: 6
Even number: 8
Even number: 10
Even number: 12
Even number: 14
Even number: 16
Even number: 18
"""
print()
"""
somewhat recent addition to the Python language 

therefore this is a newer way of making iterators, however, 
there is nothing wrong with old way and in some cases the old way is better anywway
"""

def gen():
    yield 1
    yield 2
    yield 3

print(type(gen))            # <class 'function'>
print(gen())                # <generator object gen at 0x10b55a900>

itr = gen()

print(next(itr))
print(next(itr))

for i in itr:
    print(i)

# more advanced generator: 

# suppose we want to print out the fibonacci sequence:

fib_numbers = [1, 1]

for i in range (2, 10):
    last = fib_numbers[i - 1]
    second_last = fib_numbers[i - 2]
    num = last + second_last
    fib_numbers.append(num)

print(fib_numbers)          # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

print()
# inefficient aas need to store all of the, but this works
# however, suppose we want to use a generator to do the same >>>

def fib(n):
    last = 1
    second_last = 1
    current = 3

    while current <= n:
        num = last + second_last
        yield num

        second_last = last
        last = num
        current += 1

for val in fib(10):
    print(val)              # important thing here is that whilst we have all the values, we are not storing all of them 
"""
2
3
5
8
13
21
34
55

therefore we can generate an infinite loop of numbers without storing them

therefore we might find a usecase is that we might want to create a very large or infinite number of items

you create a number and return it, you do not store all of the values (which would be a potential memory hog)

contrary, you would use the list option (not a generator) if you did want to access all of the values
"""

# P R A C T I C E

###################################
# 409.02 - what is the output
###################################

def a(lst, power):
    for element in lst:
        if element % 2 == 0:
            yield element ** power

gen = a([1, 2, 3, 4, 5, 6, 7, 8], 2)
next(gen)
next(gen)
next(gen)
print(next(gen))

"""
my guess >> 16

this was incorrect, I read the code again, initially I thought it was saying 

- divide the element by 2
- and if if divides with 0 left over
- then x to power x

therefore, only applies to even numbers, and the final sum was (8/2) = (4*4) = 16

However, when my answer was incorrect, I re-read the code and realised that the if statement was NOT dividing the numbers, 
it was only verifying that the number could be divided, before perfforming the calculation of elemnet^power

ergo, my second guess is 64 (8*8) and that was correct.

"""
###################################
# 409.03 - Range Generator
###################################
"""
write generator[ new_range ]
- when initialised, pass 3 integer value
- start, stop, step
- should mimic the range() function
"""

def new_range(start, stop, step):
    current = start

    while True:
        if step < 0 and current <= stop:
            break
        if step > 0 and current >= stop:
            break

        yield current
        current += step


##############
# solution from Programming Expert

def new_range(start, stop, step):
    for i in range(start, stop, step):
        yield i
    
# = wow!






