name = "Tim"
print(name.upper())
print(name.lower())

greeting = "Hello " + name
print(greeting)
print(len(greeting))

if name in greeting:
    print("The name is contained in the greeting!")

print(f"The first character of the name is {name[0]}")

string = """ hello
line 
line\
line
line
line
"""

print(string)

######

user_input = input("Enter an integer: ")

if user_input.isdigit():
    name = input("What is your name? ")

    print("Hello,", name.upper())
else:
    print(user_input.capitalize())

######

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

if word1 in word2:
    print("The first word is contained in the second one")
else:
    print("The first word isn't contained in the second one")

######

sentence = input("Enter a sentence: ")

words = sentence.split(" ")
number_of_words = len(words)

print(f"There are {number_of_words} words in this sentence")

#####

print("    *\n   ***\n  *****\n *******\n  *****\n   ***\n    *")
