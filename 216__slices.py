## slice allows us to get a subset of the collection (List, Tuple, etc)

my_list = [2, 3, 4, 5, 6, 7, 78]

new_list = my_list[0:2:] # you can pass [start:stop:step]
print(new_list)

new_list = my_list[:4] # note it stops before the index you define
print(new_list)

#############

student_names = ["Tim", "Antoine", "Clement", "Simon", "Alex"]
good_students = student_names[:2]
bad_students = student_names[2:]

reversed_bad_students = bad_students[::-1] # ::-1 this is a shortcut to reverse something in Python

print(f"Good students: {good_students}")
print(f"Bad students: {bad_students}")
print(f"Reversed Bad students: {reversed_bad_students}")

best_student = student_names[0]
worst_student = student_names[len(student_names) - 1]

print(f"Best student: {best_student}")
print(f"Worst student: {worst_student}")

### PRACTICE ###

### 216.09 -- modify w,x,y,z to output [8, 6, 4] ###

# w = None  # <- Change this
# x = None  # <- Change this
# y = None  # <- Change this
# z = None  # <- Change this

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# first_slice = lst[::z]
# second_slice = first_slice[:y]
# third_slice = second_slice[x:]
# last_slice = third_slice[::w]

# print(last_slice)

w = 2  # <- Change this
x = 2  # <- Change this
y = -3  # <- Change this
z = -1  # <- Change this

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_slice = lst[::z] # -1 flips the list around (reverse) 
# [10, 9, 8, .....] (we now have the list the right way)
second_slice = first_slice[:y] # -3 sets the first part of the slice to 8 (3rd item in)
# [8, 7, 6, 5, ....] (we now have the 8)
third_slice = second_slice[x:] # 2 start from 2 item later
# [_, 6] (we now have the 6)
last_slice = third_slice[::w] # 2 item later
# [ another 2 items in] ( we now have the inal item)

print(last_slice)