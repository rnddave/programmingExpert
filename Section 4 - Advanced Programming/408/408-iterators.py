"""
Iterators

iteration - again! (this time different)

iterator is a special kind of object that implements a single function [next()]

iterators historically were created through class definitions which had to 
implement the [__iter__()] method to create the iterator
in addition to the [__next()] method

However, most modern programmers opt to use the "generator" syntax nowadays due to 
increased readability and conciseness

"""

# This DividerIterator class is an iterator that will start
# at a number `start` and divide that number by `factor`
# over and over again until it is smaller than or equal
# to `end`.

class DividerIterator:
    def __init__(self, start, factor, end):
        self.start = start
        self.factor = factor
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        current = self.current
        self.current = current / self.factor
        return current


# Let's keep dividing 100 by 7 over and over again
# until 0.01.
count = 0
for n in DividerIterator(100, 7, 0.01):
    print(f"Divided {count} times: {n}")
    count += 1

"""
iterator is a special object

anything that is iterable = defines a way to get an iterator for it

we have been using this for entire course, butt we didn't mention it 


"""

x = [1, 2, 3, 4]

x_iter = iter(x)

while True:
    try:
        print(next(x_iter))
    except StopIteration:
        break

"""
1
2
3
4

the above code is basically showing us how a FOR loop works behind the scenes

x_iter = is basically the same as [x.__iter__()] - the iteration dunder method

it is iterable if it can accept the __next__() method (which is mostly hidden from the user)

"""

# let us make one ourselves

class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def __iter__(self):
        return NumberIterator(self.num1, self.num2, self.num3)

class NumberIterator: 
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.one
        elif self.current == 2:
            return self.two
        elif self.current == 3:
            return self.three
        else:
            raise StopIteration


nums = Numbers(1, 2, 3)



""" 
make it manual: 

itr = iter(nums)
print(next(itr))                # 1
print(next(itr))                # 2
print(next(itr))                # 3
print(next(itr))                # <class 'StopIteration'>

but of course we don't want to do it like this, we want a for-loop
"""
print()                         # just breaking up output from earlier code

for num in nums:
    print(num)

"""
new examples

we're going to add the iteraator into the same class
"""

class Numbers2:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.num1
        elif self.current == 2:
            return self.num2
        elif self.current == 3:
            return self.num3
        else:
            raise StopIteration












