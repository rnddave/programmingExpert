### 214.03 -- use a single for loop to print the numbers in the range of 1-10 inclusive and on separate lines ###

for i in range(1, 11):
    print(i)

### 214.03 -- alternate option ###
### 214. ###

for idx in range(10):
    print(idx + 1)


### 214.03 -- alternate option 2 ###

num = 1
for idx in range(10):
    print(num)

    num += 1

### 214.04 -- use multiple FOR loops to print each list item on a different line ###

lst = ["tim", "is", "the", "best", "instructor"]
string = "..."
tupl = ("and", "he", "is", "great")

for name_element in lst:
    print(name_element)

for char_element in string:
    print(char_element)

for word_element in tupl:
    print(word_element)

### 214.04 -- alternative ###

lst = ["tim", "is", "the", "best", "instructor"]
string = "..."
tupl = ("and", "he", "is", "great")

for idx in range(len(lst)):
    item = lst[idx]
    print(item)

for idx in range(len(string)):
    character = string[idx]
    print(character)

for idx in range(len(tupl)):
    item = tupl[idx]
    print(item)

### 214.05 -- you have 2x string, find each character that matches at same index and print that ###

string1 = "aabbcsdw"
string2 = "abbbcsdd"

for idx in range(len(string1)):
    charac1 = string1[idx] # important to note, this solution only works for strings of the same length
    charac2 = string2[idx] 

    if charac1 == charac2:
        print(charac1)

### 214.06 -- use single FOR loop to iterate through list and print elements that are both divisible by 2 and located at an odd index ###

lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

for idx in range(len(lst)): 
    item = lst[idx]

    if item % 2 == 0 and idx % 2 != 0:
        print(item)

### 214.07 -- nested FOR loops to iterate through the list, print the sum of the inner lists ###

lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

for inner_list in lst: # first we reference the inner list within lst
    sum_of_inner_list = 0 # then we create a variable to keep track (outside the sum loop)

    for item in inner_list: # now we reference each item within the inner list
        sum_of_inner_list += item # we add the sum of each item (from inner list) to the variable outside the loop

    print(sum_of_inner_list) # now print the total for this iteration of the loop, then repeat for next inner list item


### 214.08 -- single FOR loop, iterate through list of numbers, for each number, print the sum of number ###
### --------- and the sum of the number to it's right, break at the last number ###

lst = [-2, 0, 4, 5, 1, 2]

for idx in range(len(lst) - 1): # ignore the final item in the list, avoiding the 'out of bounds error'
    current_item = lst[idx] # define a 'current item'
    next_item = lst[idx + 1] # define the 'next item'

    sum_of_items = current_item + next_item # new variable for the sum of 'current' + 'next'
    print(sum_of_items) 

