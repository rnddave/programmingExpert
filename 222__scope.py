### what is Scope ###

### things defined in a function are not available outside of the function 

def foo():
    x = 6       # existing only within this function
    print(x)

foo()
# print(x)      # NameError: name 'x' is not defined

# if however, we defined x as a global variable and x within the function, then x would work for both cases (albeit with different values)
x = 9

def foo():
    x = 6       # existing only within this function === 6
    print(x)

foo()
print(x)        # === 9

#####################

name = "Tim"
was_tim_greeted = False


def say_hello(name):
    print(f"Hello {name}")
    was_tim_greeted = True


say_hello(name)

if was_tim_greeted:
    print("Tim was greeted!")
else:
    print("The variable was_tim_greeted was out of the scope of say_hello!")

### BLOCK SCOPE

imp = int(input("Enter a number: "))

#### what follows is an indentation block
if imp > 5:
    value = "Greater than 5!"   # we can access this variable (value)
else:
    value = "low value"         

print(value)

#### a function is not part of the block code, so variables existing within the function 
# are different to variable existing within the block code

def foo():
    if imp2 > 5:
        value2 = "Greater than 5!"   # we can access this variable (value)
    else:
        value2 = "low value"         

imp2 = int(input("Enter a number: "))
foo()
# print(value2)   # NameError: name 'value2' is not defined

################

def add_5(x):
    x = x + 5
    print(x)    

x = 10
print(x)        # 10
add_5(x)        # 10 + 5 (15) 
print(x)        # 10 (as we cannot change the original integer)

################ now with a list

def append_5(x):
    x.append(5)
    print(x)    

x = []
print(x)        # []    empty list
append_5(x)     # [5]   empty list +append 5  
print(x)        # [5]   lists are mutable, so the original data is also updated

################ now with a list COPY

def append_5(x):
    x = x[:]    # create a copy of the list x
    x.append(5)
    print(x)    

x = []
print(x)        # []    empty list
append_5(x)     # [5]   empty list +append 5  
print(x)        # []    remember our apped function was applied to a copy of x not the actual X

################ GLOBAL keyword

## considered bad practice, avoid at all costs, but does work... 

value = 5

def foo():
    global value 
    value = 10
    print(value)


print(value)    # 5
foo()           # 10
print(value)    # 10

### the reason this is bad practice, is because this makes debugging difficult
### it's going to change any variable outside the function with this value
