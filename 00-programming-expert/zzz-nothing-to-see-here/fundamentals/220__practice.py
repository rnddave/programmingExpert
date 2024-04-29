## 220.01 - write function takes x,y add them and return result

def add_two_arguments(x, y):
    result = x + y

    return result

x = 5
y = 4

sum_of = add_two_arguments(x, y)
print(sum_of)

# alternative solutions: 
def add(x, y):
    try:
        return x + y
    except Exception as e:
        # It can be a good practice to handle potential exceptions!
        print("Something went wrong; make sure to pass numbers to this function!")

## 220.02 - take list of integers and return a new list containing all the odd numbers from 1st list in order the appear

def find_all_odds(lst):
    odds_list = []

    for element in lst:
        if element % 2 == 1:
            odds_list.append(element)

    return odds_list

lst = [1, 2, 3, 4, 5, 6, 9, 11]

print(find_all_odds(lst))

## 220.03 -- take list of strings and return new list containing the lenghts of the strings in order of the strings entered. 

def string_lengths(strings):
        new_list = []
        
        for string in strings:
            length = len(string)
            new_list.append(length)

        return new_list

r = string_lengths(["hello", "this", "is," "a", "orange", "blue", "beard"])
print(r)

## 220.04 -- accept 2 optional parameters, return unique common elements between 2 lists. 
############ if either of the parameters isn't passed, then treat as empty list

def compare_lists(lst1=[], lst2=[]):
    
    # decalre a variable to hold the result
    lst1_set = lst1
    lst2_set = lst2

    set_same = set(lst1_set) & set(lst2_set)

    return len(set_same)

r = compare_lists([1, 2, 3], [1, 4, 3])
print(r)

# 220.04.01 alternative solutions: 

def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    set_intersection = lst1_set.intersection(lst2_set)

    return len(set_intersection)

# 220.04.02 alternative solutions: 

def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)

    set_intersection_length = 0
    for num in lst1_set:
        if num in lst2_set:
            set_intersection_length += 1

    return set_intersection_length

# 220.04.03 alternative solutions: 

def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)

    set_intersection_length = 0
    for num in lst2:
        if num in lst1_set:
            set_intersection_length += 1
            lst1_set.remove(num)

    return set_intersection_length

## 220.05 -- take a list and return new version of the list where the last elements have been removed

def trim_list(lst, elements_to_trim):
    
    for item in lst:
        newlist = lst[:-elements_to_trim or None]

        return newlist

r = trim_list([1, 2, 3, 4], 0)
print(r)

## solution 220.05.01
def trim_list(lst, elements_to_trim):
    trimmed_list = []

    for idx in range(len(lst) - elements_to_trim):
        element = lst[idx]
        trimmed_list.append(element)

    return trimmed_list
## solution 220.05.02
def trim_list(lst, elements_to_trim):
    return lst[:len(lst) - elements_to_trim]

## 220.06 -- take list of integers and return new list of the same length, where element at index i in 
############ new list is equal to numbers[0] + numbers[1] ... + numbers[i - 1] + numbers[i]

####### wtf, I don't even understand the question!! 

## this is the solution as I didn't understand the question: 

def running_sums(numbers):
    sums = []

    current_sum = 0
    for number in numbers:
        current_sum += number
        sums.append(current_sum)

    return sums

r = running_sums([1, 2, 3, 4, 68])
print(r)

## after running this piece of code, I understand what it wants is as follows: 
# take a list, then cumulatively increase each element, so that the last element is the sum of all other elements + last element

def running_sums2(nums): 
    sum_of_old_list = [] 

    current_sum = 0 

    for number in nums:
        current_sum += number
        sum_of_old_list.append(current_sum)

    return sum_of_old_list

r = running_sums2([12, 13, 2, 4, 8, 99])
print(r)