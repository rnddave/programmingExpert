"""
Generators

special kind of iterator that uses the [yeild] keyword to return the next value in a sequence
"""

# I bet you couldn't store all of those in a list! There are an
# infinite number of even numbers but generators solve this problem
# easily!
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