## Interfaces

"""
in Python, there is no formal defininition for an INTERFACE 
but we can still represent one by creating a class that only defines abstract methods 

An interface is designed to be used as an abstract data type that enforces that classes it
define specific methods and behaviour
"""

import io


class TranslatorInterface:
    def translate(self, text):
        raise NotImplementedError

    def untranslate(self, text):
        raise NotImplementedError


class SpanishTranslator(TranslatorInterface):
    def translate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hello":
                words[i] = "hola"
            elif word == "world":
                words[i] = "mundo"
        return " ".join(words)

    def untranslate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hola":
                words[i] = "hello"
            elif word == "mundo":
                words[i] = "world"
        return " ".join(words)


class FrenchTranslator(TranslatorInterface):
    def translate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hello":
                words[i] = "bonjour"
            elif word == "world":
                words[i] = "monde"
        return " ".join(words)

    def untranslate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "bonjour":
                words[i] = "hello"
            elif word == "monde":
                words[i] = "world"
        return " ".join(words)


TRANSLATORS = {
    "spanish": SpanishTranslator(),
    "french": FrenchTranslator(),
}

# In order to check that the translator works correctly, we first
# translate "hello world" into that language, and then re-translate
# the result. At the end, we should be getting "hello world" back.
def check_translator_accuracy(language):
    translator = TRANSLATORS[language]

    original_text = "hello world"
    translated = translator.translate(original_text)
    new_text = translator.untranslate(translated)

    if original_text != new_text:
        raise Exception(f"Translator {language} does not work correctly!")

    print(f"The {language} translator is correct!")


check_translator_accuracy("spanish")
check_translator_accuracy("french")

#######################################

"""
point of an interface is to outline and describe what a class that uses it should look like 

Interfaces are more important in other programming languages, we kind of just fake it in Python 

this is important to know and understand in general, moreso than in Python
"""


class RunCodeInterface:         #Interface is in the name, not mandatory, but good practice to make it stand out
    def compile_code(self):
        raise NotImplementedError("You have to implement compile_code")

    def execute_code(self):
        raise NotImplementedError("you need to implement execute_code")

    
class GoCode(RunCodeInterface):
    def comple_code(self):
        print("Compile Go Code")

    def execute_code(self):
        print("Execute Go Code")

class JavaCode(RunCodeInterface):
    def comple_code(self):
        print("Compile Java Code")

    def execute_code(self):
        print("Execute Java Code")
        

def run_code(code : RunCodeInterface):      # note the : and then the link to interface 
    code.compile_code()
    code.execute_code()

"""
python is a weakly typed programming language
"""

go = GoCode()
run_code(go)

############# PRACTICE #############

## 309.04 Shapes

import math


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError


class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length

    def get_perimeter(self):
        return self.side_length * 4


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius
