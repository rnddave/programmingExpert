# logical operators 

# and 
# or
# >
# <
# ==

# this is basically mathematics , nothing to see here... 

# can stack them up

print(1 < 2 < 3 < 4 < 5 )   # True
print(1 < 2 < 3 > 4 < 5 )   # False

# not = opposite basically

print(not(True))    # False 
# this is because we're saying that we want the opposite of True

print(not(1))       # False
# (remember Truthy Falsey)

print(not(1 > 2))   # True  
# 1 is NOT > 2 = True

#-------------------------------
# something different 

is_magician = False
is_expert = True

# check if Magician AND expert = You are a Master Magician
# if Magician but NOT expert = you are on the right path
# if NOT magician = You need some Magic

if is_magician and is_expert:
    print('You are a Master Magician')
elif is_magician and not(is_expert):    # actually doesn't need the brackets in the NOT
    print('You are on the right path')
elif not(is_magician):
    print('You need some magic in your life')
