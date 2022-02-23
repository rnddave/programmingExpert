a = 1
while a != 42:
    print("a is still not 42")
    a += 1

### same as FOR Loops, but with extra use-cases, as in 'whilst something is true' 

x = 0
while x < 5:
    x += 1
    print(x)

### why not use the FOR Loop? 
### If you don't know how many times you want to run the loop, you use a WHILE loop

### vs a FOR Loop where you always know how many times to run, even if you don't know 
### the size of the list for example, you would use in range(len(lst)) which defines the number of times it will run

### a while loop will run until a condition is met (something becomes True)
### perhaps easier to consider the value of a WHILE loop when you allow users to input data - you may not know what they will input until runtime

num = input("enter an integer: ")

while not num.isdigit():
    num = input("enter an integer: ")
    # we don't know how many takes it will be before a user does what we want, therefore, a FOR loop will not work

# we can make this loop better to avoid writing the same line both inside and outside the loop: 

while True: 
    num = input("enter an integer: ")
    if num.isdigit():
        break

### breaking a while loop when a number reaches a sum ###

lst = [1, 2, 3, 5, 6, 4] # define the list

result = 0 # define a variable to hold the sum
i = 0 # define an index variable

while result < 9 and i < (len(lst)): # while the sum is less than 9 (and that we don't reach the end of the list (index))
    num = lst[i] #define a new variable that links the number (the list element) with the index item
    result += num # add the list element to the result variable
    i += 1 # increment the index

    print(num)

### WHILE ELSE ####

lst = [1, 2, 3, 5, 6, 4] # define the list
i = 0

while i < len(lst):
    if lst[i] == -2:
        print("found it")
        break
    i += 1
else:
    print("didn't find it")