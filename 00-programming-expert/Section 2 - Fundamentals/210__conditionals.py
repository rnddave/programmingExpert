a = 1
b = 2

if a == 1:
    print("a is equal to 1")

if b == 1:
    print("b is equal to 1")
elif b == 2:
    print("b is equal to 2")
else:
    print("b is not equal to 1 and not equal to 2")

# test yourself

age = int(input("How old are you? "))

if age >= 13:
    print("You can ride the roller coaster!")
else:
    print("You can't ride the roller coaster.")

# test number 2

fav_language = input("What's your favorite programming language? ")

if fav_language == "Python":
    print("Nice choice!")
elif fav_language == "Golang":
    print("You're a cool kid I see...")
elif fav_language == "JavaScript":
    print("Okay Mr. web developer.")
else:
    print("I don't know that language.")

# test number 3

number1 = float(input("Enter a number: "))
# we use float() instead of int() to make sure if the user
# enters a float like: 2.1, 0.3 or 4.5 the program doesn't crash

if number1 >= 10 and number1 <= 20:
    number2 = float(input("Enter another number: "))
    sum_of_numbers = number1 + number2

    print("The sum of these two numbers is:", sum_of_numbers)

    if sum_of_numbers > 100:
        print("That is a large sum!")