# Sets are collections of unique items, you can create, add to and remove from a set, but like dictionaries, 
# they are unordered therefore, iterating through a set is not gauranteed to give you the same results each time

sentence = (
    "This is a regular sentence with words inside. Some words are unique within the sentence, "
    + "while some are duplicates."
)
words_with_duplicates = sentence.split(" ")
unique_words = set(words_with_duplicates)

print(words_with_duplicates)
print(unique_words)
print(f"The sentence contains {len(unique_words)} unique words, but {len(words_with_duplicates)} words total.")

###########

# interestingly, the set has to be unique, you will never see a duplicate item?? 

x = set() # you have to declare the set() funtion because a set also uses {}, but if you do not define it as a set, python will assume you want a dictionary
y = {}
print(type(x)) # output = <class 'set'>
print(type(y)) # output = <class 'dict'>

#####

z = {1, 2, 3, 1, 2, 1, 2} # if you start with a pre-populated list, then you can use the {} but note, there is no key/value pairing
print(type(z)) # output = <class 'set'>
print(z) # output = {1, 2, 3} == NB there are no duplicates listed here

## to add something to your set: 
z.add(4) # note that we use "add" NOT append!
print(z) # modified z
z.add(4) # add another z
print(z) # note that we only see 1x 4 because, again, we cannot store duplicates in a set

## now to remove an element
z.remove(3)
print(z) # {1, 2, 4}
# warning, cannot remove an item that doesn't exist

## clear a set
z.clear()
print(z) # set()

## lenght
z.update([1, 2, 3, 1, 2, 3]) # this is just me re-populating the cleared set with new data
print(z)
print(len(z))

### NB you can add any item to a set, but you cannot add a list inside a set as follows: 

e = {1, 2, 3, 4, "hello", True, 0.2, (1, 2)} # NB whilst you cannot have a LIST inside a set, you can have a Tuple
print(e) # output = {0.2, 1, 2, 3, 4, (1, 2), 'hello'} (interesting the order is different)

## okay, now to find something in a set

contains = 1 in e
print(contains) # True
# a lookup of a set is almost instant

## using the union()

x = {1, 2}
y = {2, 3}

z = x.union(y)
print(z) # new set
print(x) # shows that the x set remains untouched

# alternative to using union() = | 
g = x | y # this only works on sets
print(g) # {1, 2, 3}

## intersection = of 2 sets, simply the items in both sets (as in items that are duplicated)
x = {1, 2, 3}
y = {2, 3, 4}
f = x.intersection(y)
print(f) # {2, 3} <-- you will note, this only prints out the numbers that match in both sets (1, 4 are missing)
# there is an alternative to this as well: 
ll = y & x
print(ll) # {2, 3}

## difference - this shows us what is different, but the order of the syntax is important here: 
dif = x.difference(y)
print(dif)    # {1}
dif2 = y.difference(x)
print(dif2)    # {4}
# alternative = the "-"
dif3 = x - y
print(dif3)    # {1}

## symmetric difference = the elements that are not shared between the sets
x = {1, 2, 3}
y = {2, 3, 4}
f2 = x.symmetric_difference(y) # the order of this statement is not as important as 'difference'
print(f2)      # {1, 4}
# alternative 
f3 = x ^ y
print(f3)

## using the update()
x = {1, 2, 3}
y = {2, 3, 4}
print(x, y)    # {1, 2, 3} {2, 3, 4}

x.update(y)
print(x, y)     # {1, 2, 3, 4} {2, 3, 4}

## and to add a difference_update: 
x2 = {1, 2, 3}
y2 = {2, 3, 4}
print(x2, y2)    # {1, 2, 3} {2, 3, 4}

x2.difference_update(y2)
print(x2, y2)     # {1} {2, 3, 4} ## x2 is updated to remove the common elements

## symmetric_update
x3 = {1, 2, 3}
y3 = {2, 3, 4}
print(x3, y3)    # {1, 2, 3} {2, 3, 4}

x3.symmetric_difference_update(y3)
print(x3, y3)     # {1, 4} {2, 3, 4}

#####################

## subset and superset
m = {1, 2, 3, 4} # m has all the elements of n + more = superset
n = {1, 2, 3} # n has some of the elements of m, which means it is a subset of m

# however, if we modify the subset, so that it no longer has all elements of the superset, even if only one change
# then the subset/superset relationship is broken 
m2 = {1, 2, 3, 4, 5, 6, 7} 
n2 = {1, 2, 3, 8} # because 8 is not in m2, the subset/superset relationship is broken

# with such small sets, it's easy to see this as a human, but a computer sees it differently, and if the sets were larger, 
# it might even be hard for a human, therefore, python can help us with this
print(n.issubset(m)) # True
print(m2.issuperset(n2)) # False

# there are alternatives for this as well:
print(n <= m) # True
print(m >= n) # True
print(m2 >= n2) # False

## Set Theory = proper-superset, proper-subset = proper = means it has at least 1 other element (cannot match)
print(m < n) # False
print(m > n) # True

o = m | n       # declaring new variables that will be the same
l = n | m
print(o <= l)   # check if o is a subset of l + has the same elements (but don't check if the same)
print(o >= l)   # check if l is a superset of o + has the same elements (but don't check if the same)
print(o < l)    # line 152 = True, but is it a proper subset? = FALSE = because l doesn't have at least 1 more element

##################################
## now for some examples

x = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 5, 6]
print(x, type(x))           # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 5, 6] <class 'list'>
# if I wanted to know all the unique numbers, I'd need a loop to work through the list
# alternative is to change it into a set
set_x = set(x)
print(set_x, type(set_x))   # {1, 2, 3, 4, 5, 6} <class 'set'>

# if for some reason I wanted a list of unique numbers, I can convert it back to a list: 
set_x2 = list(set(x))
print(set_x2, type(set_x2)) # [1, 2, 3, 4, 5, 6] <class 'list'>

## get some numbers and make sure I don't get duplicate.

numbers = set()

while True:
    num = int(input("Numbers: "))

    if num in numbers:
        break

    numbers.add(num)

print(numbers)

## however, when to use a set vs a dictionary? 
# set = only care if something exists or not, you don't care about the frequency or order
# set = I don't know when or where it was inserted
# dictionary = tells you the frequency something comes in
# dictionary gives you the ability to hold additional information

######################## some PRACTICE ########################

## ask user to enter characters until enters a previously entered character, or more than one character at a time
## then print the number of unique characters

# create empty set
chars = set() 
# get input from the user (in a loop)
while True: 
    char = input("Enter a character: ")

# quit if a duplicate letter entered OR if user enters multiple characters in single entry 
    if char in chars or len(char) >1:
        break

    chars.add(char)
# print number unique characters
print(f"Number of unique characters entered: {len(chars)}")

#### solution from exercise: -- basically the same, except use 2x if statements

characters = set()

while True:
    character = input("Enter a character: ")
    if len(character) > 1:
        break

    if character in characters:
        break

    characters.add(character)

print(f"Number of unique characters entered: {len(characters)}")







