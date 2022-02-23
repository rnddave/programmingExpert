## Sort Employees

# write a function that accepts a list of lists that contain the name, age, salary of specific employees
# and also accepts a string representing the key to sort employees by
# your function should return a new list that contatins the lists representing each employee
# sorted in ascending order by the given key

# (1) define function to sort employees
# (2) take input from user (sorting key)
# (1.b) Make a new list, sort the employees by the key provided and display

employees = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000],
]

def sort_employees(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    return sorted_employees

sort_by = input("Sort by what (age, name, salary)? ")

r = sort_employees(employees, sort_by)
print(r)

####### alternate solution: 

# Copyright © 2021 AlgoExpert LLC. All rights reserved.

def sort_employees(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = []
    # Copy the employees list so we don't modify it
    employees_copy = employees[:]

    while len(employees_copy) > 0:
        smallest_employee_index = 0

        for i, employee in enumerate(employees_copy):
            current_smallest_value = employees_copy[smallest_employee_index][sort_index]
            if employee[sort_index] < current_smallest_value:
                smallest_employee_index = i

        # After looking through all remaining employees we will have found the employee
        # with the smallest sort_by value so we add it to the sorted list
        next_sorted_employee = employees_copy[smallest_employee_index]
        sorted_employees.append(next_sorted_employee)
        employees_copy.pop(smallest_employee_index)

    return sorted_employees
