## Caesar Cipher

# write a function that accepts a string and returns the caesar cipher encoding of that string 
# according to a secondary input parameter 

# this involves shifting each character of the string a set number of positions PREVIOUS in alphabet

# (1) get a string input
# (2) get am offset input
# (3) FUNCTION convert the string per the offset

def cipher(stringIn, offset):
    result = ""
    for i in range(len(stringIn)):
        char = stringIn[i]
        result += chr((ord(char) - offset - 97) % 26 + 97)
    
    return result

# (1) get a string input
stringIn = input("string ")

# (2) get am offset input
offset = int(input("offset "))

r = cipher(stringIn, offset)
print(r)

###### tests from the interface ######

# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

# import program
# import unittest


# class TestProgram(unittest.TestCase):
#     def test_case_1(self):
#         string = "hello"
#         offset = 3
#         expected = "ebiil"
#         result = program.caesar_cipher(string, offset)
#         self.assertEqual(expected, result)

#     def test_case_2(self):
#         string = "apple"
#         offset = 0
#         expected = "apple"
#         result = program.caesar_cipher(string, offset)
#         self.assertEqual(expected, result)

#     def test_case_3(self):
#         string = "abc"
#         offset = 20
#         expected = "ghi"
#         result = program.caesar_cipher(string, offset)
#         self.assertEqual(expected, result)

#     def test_case_4(self):
#         string = ""
#         offset = 3
#         expected = ""
#         result = program.caesar_cipher(string, offset)
#         self.assertEqual(expected, result)

#     def test_case_5(self):
#         string = "a"
#         offset = 26
#         expected = "a"
#         result = program.caesar_cipher(string, offset)
#         self.assertEqual(expected, result)

#     def test_case_6(self):
#         string = "hagshsah"
#         offset = 8
#         expected = "zsykzksz"
#         result = program.caesar_cipher(string, offset)
#         self.assertEqual(expected, result)

############# proposed solution from AlgoExpert:::: 

# Copyright © 2021 AlgoExpert LLC. All rights reserved.

def caesar_cipher(string, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    encoded_string = ''

    for character in string:
        position = alphabet.index(character)
        offset_position = position - offset
        # No need to handle negative positions because of negative indexing
        encoded_character = alphabet[offset_position]
        encoded_string += encoded_character

    return encoded_string
