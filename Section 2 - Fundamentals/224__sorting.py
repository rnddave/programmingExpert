strings = ["Google", "Microsoft", "Netflix", "Apple", "Amazon"]
print("Sorted strings:", sorted(strings, reverse=True))
print("Unsorted strings:", strings)

strings.sort()
print("Sorted strings:", strings)

################

# sorted() return a new list containing all items in iterable in ascending order
print("Sorted \n")
lst = [1, 2, 4, 1, 3, 1, 5, 2]
print(lst)          # [1, 2, 4, 1, 3, 1, 5, 2]
print(sorted(lst))  # [1, 1, 1, 2, 2, 3, 4, 5]
print(lst)          # [1, 2, 4, 1, 3, 1, 5, 2]  === list remains untouched

# sort()    sorts the actual list, not create a new list
print("\n sort\n")
lst = [1, 2, 4, 1, 3, 1, 5, 2]
print(lst)      # [1, 2, 4, 1, 3, 1, 5, 2]
lst.sort()
print(lst)      # [1, 1, 1, 2, 2, 3, 4, 5]      === list is now sorted, cannot be unsorted.... 

######## default sort = ascending
print("\nReverse sort \n")
lst.sort(reverse=True)
print(lst)      # [5, 4, 3, 2, 2, 1, 1, 1]

######## default sorted = ascending
print("\nReverse sorted \n")
lst = [1, 2, 4, 1, 3, 1, 5, 2]
print(sorted(lst, reverse=True))    # [5, 4, 3, 2, 2, 1, 1, 1]
print(lst)                          # again, original list is untouched

######## sorted = TUPLE
print("\nReverse sorted TUPLE \n")
lst = (1, 2, 4, 1, 3, 1, 5, 2)
print(sorted(lst, reverse=True))    # [5, 4, 3, 2, 2, 1, 1, 1] = a list, so if you wanted it as a tuple, you need to convert it
print(lst)                          

print(tuple(sorted(lst, reverse=True)))    # (5, 4, 3, 2, 2, 1, 1, 1)

#### cannot use sort() with tuples, as they are immutable, remember, sorted, makes a caopy, does not modify original

print("\n\n\n\n")
lst = [[1,2], [3, 4], [4, 5], [-1, -5]]
lst.sort()
print(lst)

# but what if you wanted to sort a different way, perhaps by the second element for example? 

def sort_second_index(item):
    return item[1]

lst = [[1,2], [3, 4], [4, 5], [-1, -5]]
lst.sort(reverse=True, key=sort_second_index)
print(lst)