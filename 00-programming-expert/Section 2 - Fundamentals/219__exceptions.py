## exceptions in python are basically errors, i.e. something unexpected happened

## usually an exception is unexpected, but if there are parts of your code that you think might face challenge 
# you can avoid the exception by using TRY and EXCEPT

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    if len(digits) != 10:
        raise Exception("There should be exactly 10 digits!")
except Exception as e:
    print(e)
finally:
    print("Goodbye!")

############
# we can write our own exceptions, this is useful if someone else is using our code, it turns them what went wrong. 

## handle exceptions = Try/Except
try: 
    int("hello") # you can't have a STRING in and INTEGER, therefore, this should fail, but try, allows it to move to our exception
except: 
    print("Exception") # Exception
print("done")

# you could build on this by asking for the value of the exception: 
try: 
    int("hello") 
except ValueError as e: 
    print("Exception", e) # Exception invalid literal for int() with base 10: 'hello'
print("done")

### what about multiple errors? 
try: 
    2 / 0                               # note this changed for this example
except ValueError as e: 
    print("Value Exception >>", e)      # this exception is not met, move to next
except ZeroDivisionError as e: 
    print("Zero Div Exception >>", e)   # Zero Div Exception >> division by zero
print("done")

### what about generic errors
try: 
    2 / 0                                   # divide by 0
except Exception as e:                      # this is a general exception (kind of makes the other exception types seem useless?)
    print("An Exception Occurred >>", e)    # An Exception Occurred >> division by zero
print("done")
                                            # typically in python it is not a good idea to accept the general exception as you won't know how to debug it...

### FINALLY
try: 
    2 / 0                                   # divide by 0
except Exception as e:                      # 
    print("An Exception Occurred >>", e)    # An Exception Occurred >> division by zero
finally:                                    # this ensures program will continue and run anyway, basically ignore the error
    print("done")                           # this is kind of a clean-up operation, you can use try to check something, 
                                            # if it doesn't work then pass your prefered answer back anyway

### raising own errors RAISE
# raise ValueError("This is an error!") # (comment this out to allow prog to run) after test

# perhaps you don't know what type of error: 
# raise Exception("This is an exception") # (comment out after testing)

##############

num = input("Enter a number: ")

if not num.isdigit():
    raise ValueError("This is not a valid number")

##############

while True:
    num = input("Enter a number: ")

    try:
        num = float(num)
        break
    except ValueError:
        print("This is not a FLOAT, try again!")

#######################
# Run Time vs Compile Time

# compile = convert source code to byte code (so comp can understand it)
# errors can occur at compile time - syntax errors

# print("hello" # SyntaxError: unexpected EOF while parsing
# the program cannot even compile 

# runtime errors are harder to find. 

###################### PRACTICE ######################

### 219.05
# ask for 2 numbers (numerator & denominator), divide the numerator by the denominator
# handle exceptions as a result of the division
# specifically, catch non-numbers or the denominator is a 0
# if no exceptions, prog should print result of division and tell user goodbye! 

# You'll have to use the following strings:
print("\n\nWelcome to my division thingy\n\n")
# 1) "Enter the numerator: "
num = int(input("Enter the numerator: "))

# 3) "The numerator is not a number."
while True:
    try:
        num = int(num)
        break
    except ValueError:
        print("The numerator is not a number.")

# 2) "Enter the denominator: "
denum = num = int(input("Enter the denominator: "))

# 4) "The denominator is not a number."
while True:
    try:
        denum = int(denum)
        break
    except ValueError:
        print("The denominator is not a number.")
# 5) "You cannot divide by 0."
    except ZeroDivisionError:
        print("You cannot divide by 0.")
# 6) "This division cannot be performed."
        print("This division cannot be performed.")

    result = num / denum
    # 7) "The result of this division is _."
    print(f"The result of this division is {result}.")
# 8) "Goodbye!"
print("Goodbye!")

############## MINE DID NOT WORK: SOLUTIONS: 

numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    numerator = float(numerator)
except Exception as e:
    print("The numerator is not a number.")

try:
    denominator = float(denominator)
except Exception as e:
    print("The denominator is not a number.")


try:
    result = numerator / denominator
    print(f"The result of this division is {result}.")
except ZeroDivisionError as e:
    print("You cannot divide by 0.")
    print("This division cannot be performed.")
except Exception as e:
    print("This division cannot be performed.")
finally:
    print('Goodbye!')

############# solution 2

numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    numerator = float(numerator)
except Exception as e:
    print("The numerator is not a number.")

try:
    denominator = float(denominator)
    if denominator == 0:
        print("You cannot divide by 0.")
except Exception as e:
    print("The denominator is not a number.")


try:
    result = numerator / denominator
    print(f"The result of this division is {result}.")
except Exception as e:
    print("This division cannot be performed.")
finally:
    print('Goodbye!')
