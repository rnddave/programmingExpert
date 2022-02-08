"""
402.2 >> Reading Files

open a file called [programmingExpert.txt] that is located in the data directory
and print how many words are in the file

Escape characters (\n, \t) and periods, commas and dashes are not considered words

"""

# file = open("data/programmingExpert.txt", "r")

# let me see what the file looks like to begin >> 
file = open("programmingExpert.txt", "r")
letMeSee = file.read()
print(letMeSee)

# now, let's try counting the 'words' in the file

letMeSeeWordCount = letMeSee.split()
print(len(letMeSeeWordCount))                   # 180

# but we know we have some escape characters in there (although I am not seeing the \n, \t)
# so let's clean that up: 

file = open("programmingExpert.txt", "r")
letMeSee = file.read()

escapeCharacters = letMeSee.replace("\n", " ")
punctuation = escapeCharacters.replace(",", "").replace("-", "").replace(".", "")

print(len(punctuation))                         # 996
                                                # = seems I am now counting characters?

words = punctuation.split()
print(len(words))                               # 179

# _+_+_+_+_+_+_+_+_+_+_+_+_

"""
This above passed the code test, as follows in the proposed solutions
"""

# solution 1

text = ""

with open("data/programmingExpert.txt", "r") as file:
    text = file.read()

escape_characters_removed = text.replace("\n", " ")
punctuation_removed = escape_characters_removed.replace(
    ",", "").replace("-", "").replace(".", "")

words = punctuation_removed.split(" ")
empty_strings = words.count("")
number_of_words = len(words) - empty_strings

print(number_of_words)

# solution 2

file = open("data/programmingExpert.txt", "r")
text = file.read()
file.close()

escape_characters_removed = text.replace("\n", " ")
punctuation_removed = escape_characters_removed.replace(
    ",", "").replace("-", "").replace(".", "")

words = punctuation_removed.split(" ")
empty_strings = words.count("")
number_of_words = len(words) - empty_strings

print(number_of_words)
