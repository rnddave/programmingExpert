# short circuiting


is_friend = True
is_user = True

# short circuiting is like an OR short condition 

print(is_friend or is_user)    # True

if is_friend or is_user:
    print('are you my bff?')    # are you my bff?

# it is more effienct than and (if you only need one answer) because if the first condition is True 
# - then we don't care about the second condition, so we short circuit the answer

