basket8 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7]

print(basket8.count(5)) # count's how many times a vaule appears in a list = in this case = 3

basket9 = [ 1, 1, 3, 4, 5, 6, 7, 8, 1, 2, 4, 5, 5, 5, 1, 9, 10, 11, 12, 2, 2, 2, 2, 3, 3, 3, 3, 6, 6, 6, 6, 7, 7 ]

print(basket9)
# [1, 1, 3, 4, 5, 6, 7, 8, 1, 2, 4, 5, 5, 5, 1, 9, 10, 11, 12, 2, 2, 2, 2, 3, 3, 3, 3, 6, 6, 6, 6, 7, 7]

basket9.sort()
print(basket9)
# [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 9, 10, 11, 12]


# basket10 = ['1a', 'a2', 'b', 3, 4, '5e', 'f6'] --- this CAN'T SORT AS CANOT SORT BETWEEN INT and STRING

### try again, using some other values
basket10 = ['1a', 'a2', 'b', '3c', 'd4', '5e', 'f6'] # just wonder how sorting will look
basket10.sort()
print(basket10) # ['1a', '3c', '5e', 'a2', 'b', 'd4', 'f6']

### guessing this is an ASCII sort

basket11 = ['A', 'MN', 'o', 'O', '1', 'A1', 'a1', 'bbb', 'iJK', 'L' 'BV', 'B', 'CDE', 'fgh']
basket11.sort()
print(basket11) # ['1', 'A', 'A1', 'B', 'CDE', 'LBV', 'MN', 'O', 'a1', 'bbb', 'fgh', 'iJK', 'o']
# indeed this looks like an ASCII sort

# SORTED is something that produces a new array!!!!

basket12 = ['1a', 'a2', 'b', '3c', 'd4', '5e', 'f6']

print(basket12, sorted(basket12)) 
# ['1a', 'a2', 'b', '3c', 'd4', '5e', 'f6'] 
# ['1a', '3c', '5e', 'a2', 'b', 'd4', 'f6']

basket13 = sorted(basket12)
print(basket12, basket13)
# ['1a', 'a2', 'b', '3c', 'd4', '5e', 'f6'] 
# ['1a', '3c', '5e', 'a2', 'b', 'd4', 'f6']

############

# let's do a reverse sorted list

basket12.sort()
basket12.reverse()
print(basket12) # ['f6', 'd4', 'b', 'a2', '5e', '3c', '1a']

