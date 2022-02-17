###################################
# 400.03 - GENERATE STRING
###################################

"""
write a generator 
- accepts a string and an integer called [frequency]
-- generate sequence as follows
--- [string[0] * frequency + string[1] * frequency + ... + string[-2] * frequency + string[-1] * frequency]

- your generaor should NOT store this string, it should generate the next element in the sequence each time its [next] method is called 

- you should create this generator in both a functional and class based was

- functional should be named [generate_string]
- class should be named [GenerateString]

you may assume that frequency will allywas be >= 0


STARTING CODE >>> 

def generate_string(string, frequency):
    # Write your code here.
    pass


class GenerateString:
    def __init__(self, string, frequency):
        # Write your code here.
        pass

    # Write your code here.

=============================================


"""

# WTF - I DON"T even UNDERSTAND the question!!!!!!!!



def generate_string(string, frequency):
    for char_in_string in string:
        for char_per_freq in range(frequency):
            yield char_in_string


"""
for i in generate_string("blue", 5):
    print(i, end="")


>>> output

bbbbbllllluuuuueeeee

THIS bit SEEMS to be working fine

"""



class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.char_in_string = 0
        self.char_count = 0

        return self

    def __next__(self):

        if self.char_count >= self.frequency:
            self.char_count = 0
            self.char_in_string += 1

        if self.char_in_string >= len(self.string):
            raise StopIteration

        self.char_count += 1

        return self.string[self.char_in_string]

###################################
# 400.03 - GENERATE STRING              SOLUTION
###################################


def generate_string(string, frequency):
    for char in string:
        for _ in range(frequency):
            yield char


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.current_char_index = 0
        self.char_counter = 0
        return self

    def __next__(self):
        if self.char_counter >= self.frequency:
            self.char_counter = 0
            self.current_char_index += 1

        if self.current_char_index >= len(self.string):
            raise StopIteration

        self.char_counter += 1
        return self.string[self.current_char_index]


