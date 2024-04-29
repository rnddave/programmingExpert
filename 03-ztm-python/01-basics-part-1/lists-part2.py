basket4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

basket5 = basket4

print(basket5)

basket5.clear()
print(basket5, type(basket5))  # [] <class 'list'>

###########

# lists are complicated in Python, above looks like I created a new list called basket5 and then cleared backet 5
# in fact what I did was create a new pointer to the same memory location
# therefore basket4 and basket5 have unique names but reference the same piece of memory
# the tricky bit here is that when I cleared basket5, I also cleared basket4

###########

# creating a duplicate lists in unique memory objects. 

basket6 = ['i', 'am', 'basket', 6]
print(basket6)

basket7 = basket6.copy()
basket7.append(7)
basket7.remove(6)
print(basket6, basket7)

# looking at the index again
print(basket7)
print(basket7.index('am')) # this will tell me which index has 'am'

# but what if you don't know if the word is even in the list? 
# KEYWORDS
# https://www.w3schools.com/python/python_ref_keywords.asp
# we're going to use the keyword in

print('am' in basket6) # True








