#lesson 14; for loops
print("lesson 14; for loops")

numbers = []

for j in range(5, 25, 5): # (start, number of items, interval)
    num = input("Enter a num: ")
    numbers.append(int(num))

print(numbers)

# break

print("lesson 14; for loops - looping through lists")

lst = [1, 2, 3, 4, 5, True]

for idx in range(len(lst)): # this looks at the (len) function to auto find the end of the list 
    print(lst[idx]) # this is looping through the indices of the list

# break

print("lesson 14; for loops - iteration by item")

lst = [1, 2, 3, 4, 5, True]

for element in lst: # this iterates by elements within the list, you do not need to know the size of the list to begin 
    print(element) # this is looping through the elements

# break

# enumerate

print("Supposing we want to see both the index of the elemnet and the element itself, we introduce the enumerate keyword")

for i, elemnet in enumerate(lst):
    print(i, element)

# looping through strings and tuples

tup = (2, 5, 6, "hello", "tim", True)

for i in range(len(tup)):
    element = tup[i]
    print(element)

for element in tup:
    print(element)

for i, element in enumerate(tup):
    print (i, element)

s = "My String"

for i in range(len(s)):
    print(s[i])

# if I wanted every other character

s = "My String"

for i in range(0, len(s), 2): # (0 = start at first item, len(s) = allow it to figure out size of list, 2 = every other item)
    print(s[i])

# using the break keyword, example, going through a list until you find an item you want to break at

lst2 = [1, 2, 3, 4, 5, 4, 2, 5, 7]

for num in lst2:
    if num == 4:
        break
    print(num)

print("done")

# using the continue keyword
# kind of like the break, it finds what you want to find, but then skips it and continues with the list

lst3 = [1, 2, 3, 4, 5, 4, 2, 5, 7]

for num in lst3:
    if num == 4:
        continue
    print(num)

print("done")


### nested for loops (to loop through a nested list) ###

for i in range(10):
    for j in range(10):
        for w in range(10):
            print(i, j, w)


lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

for i in range(len(lst)):
    interior_list = lst[i]
    for j in range(len(interior_list)):
        print(interior_list[j])

### find if a letter exists in a string, and then indicate it's index ###

st = "hello world"

for i, char in enumerate(st):
    if char == "w":
        print(i)


### use a for loop to build up a list, or append to a list ###

numbers = [] # important to remember in this type of loop, the list needs to be outside the loop, else will be reinstantiated at each loop

for i in range(3):
    num = input("Enter a number: ")
    numbers.append(int(num))

print(numbers)

### the pass keyword -- acts as a place-holder, this allows you to use build a For loop etc without having to build it completely ###

for i in range(3): # this : tells the compiler to expect some condition statements, but...
    pass # having this keyword will allow the program to run, without this for loop being completed 

### For Else statements ###

print("n\n\n\n Using For Else statements \n\n\n")

words = ("hello", "world", "this", "is", "me")
target = "me"

for word in words:
    if word == target:
        print("I found the word!")
        break

else:
    print("I didn't find the word!!")




