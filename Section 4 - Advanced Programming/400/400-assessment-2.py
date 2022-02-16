###################################
# 400.02- INTEGER SUM
###################################

"""
write a function called [integer_sum]
- accept any number of positional arguments (assumed to be integers)
- function to return the sum of all these integers

HOWEVER - error handling >>> 
- write following decorators
-- [flatten_lists] = flatten any [list] arguments
--- extract elements, pass them as individual arguments instead of a list
--- remove any non-integer components of the list

-- [convert_string_to_ints]
--- convert any string arguments that are valid integers to integers
--- pass them to the decorated function
--- remove any non-integer components from the string

-- [filter_integers]
--- decorator should remove any argument that iis not an integer
--- then call the decorated function with only integer arguments
"""

