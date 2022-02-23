class Instructor:
    def __init__(self, name):
        self.name = name


tim = Instructor("Tim")

########## objects
# in python, object is the class all other classes inherrit from, even if it wasn't declared explicitly by the programmer
# objects = the interactions of objects within a program 
# almost everything in python is an object (functions, lists, ints, etc) 

x = 1   # x is an object of type int (an instance) with the value 1 
print(type(x))      # <class 'int'> == CLASS, an object

y = "string"
print(y.upper())    # STRING    == a class that defines 'string' data type, has a method called upper()

def foo():
    print("hello")

print(type(foo))    # <class 'function'> == a class is a blueprint for how it works within a program

## instance = existance of an object date type
y2 = "hello"        # an instance of the class() string

## method = like a function that you call on the instance of a class
st = "string"
print(st.upper())

