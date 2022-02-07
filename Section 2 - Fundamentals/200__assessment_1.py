# random number guesser

# (1) ask for 2x integer (represent start and end of a range) 
# (2) program should then generate a random number 
# (3) ask the user to guess the randomly generated number
# (4) Once user guesses correct random number, tell user how many attempts this took

import random

# (1) ask for 2x integer (represent start and end of a range) 

startnum = input("Enter the start of the range: ")
while not startnum.isdigit():
    try:
        startnum = input("Enter the start of the range: ")
        break
    except ValueError:
        print("Please enter a valid number.")

endnum = input("Enter the end of the range: ")
while not endnum.isdigit():
    try:
        endnum = input("Enter the end of the range: ")
        break
    except ValueError:
        print("Please enter a valid number.")

# (2) program should then generate a random number 

random_num = random.randint(int(startnum), int(endnum))
# print(f"rand_int = {random_num}")

# (3) ask the user to guess the randomly generated number

userGuess = None
number_of_entries = 0

while userGuess != random_num:
    guess = input("Guess a number: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    number_of_entries += 1
    userGuess = int(guess)

# (4) Once user guesses correct random number, tell user how many attempts this took

suffix = ""
if number_of_entries > 1:
    suffix = "s"

print(f"You guessed the number in {number_of_entries} attempt{'s'[:number_of_entries^1]}")

########### SOLUTION FROM PE.io

# Copyright © 2021 AlgoExpert LLC. All rights reserved.

import random

start = input('Enter the start of the range: ')
while not start.isdigit():
    print('Please enter a valid number.')
    start = input('Enter the start of the range: ')

end = input('Enter the end of the range: ')
while not end.isdigit() or int(end) < int(start):
    print('Please enter a valid number.')
    end = input('Enter the end of the range: ')

random_number = random.randint(int(start), int(end))

guess = None
attempts = 0

while guess != random_number:
    guessed_number = input("Guess a number: ")
    if not guessed_number.isdigit():
        print("Please enter a valid number.")
        continue
    
    attempts += 1
    guess = int(guessed_number)

suffix = ""
if attempts > 1:
    suffix = "s"

print(f'You guessed the number in {attempts} attempt{suffix}')
