class Instructor:
    def __init__(self, name):
        self.name = name


tim = Instructor("Tim")
print(tim.name)

##### attributes
"""
an attribute  is an object that belongs either to a class, or to an instance of that class. 

Attributes of an object can be referenced using [.] notation

class attributes are attributes that are shared by all instances of that class while 
instance attributes may have a different value for each and every instance that was created
"""

#### Constructor
"""
constructor of a class is a function defined within the class definition that will be
called when a new instance is created. in Python, the constructor is implemented with the __init__ method

typically the constructor is responsible for initialising any instance variables, 
and essentially prepares the instance for use by the rest of the program
"""

#### Instance
"""
an instance of a class is an object created from that classes blueprint
"""

#### Encapsulation
"""
encapsualtion in OOP refers to how a programmer might prevent outside access to the details of a class
in order to simplify the way the class might be used, 
or to make it harder to misuse the functionality that is exposed through certain methods or properties 
"""

####################

# creating our own class

class Person:       # convention = "Pascal Case" which is like camelCase but the first letter is also a capital
    pass

p1 = Person()       # instanciate the class (but remember this class is basically useless at moment)
print(p1)           # <__main__.Person object at 0x101bf5cd0> ## this gibberish is the memory address for the instance

### initialising the class

class Person2:       # convention = "Pascal Case" which is like camelCase but the first letter is also a capital
    def __init__(self):
        print("Person2 is running")

p2 = Person2()

class Person3:       # convention = "Pascal Case" which is like camelCase but the first letter is also a capital
    def __init__(self, x):
        print("Person3 is running")
        print(x)

p3 = Person3("David")
p3b = Person3("Colin")

class Person4:       # convention = "Pascal Case" which is like camelCase but the first letter is also a capital
    def __init__(self, name):
        print("Person4 is running")
        self.name = name
        print(self.name)

p4 = Person4("David")
p4b = Person4("Colin")

#### the self keyword
"""
self = parameter

need to be in all methods, but especially the __init__
"""
print(p4.name)
print(p4b.name)

#### making more attributes

class Person5:       # convention = "Pascal Case" which is like camelCase but the first letter is also a capital
    def __init__(self, name, age):
        print("Person5 is running")
        self.name = name    # these attributes are attached to the instance not the class
        self.age = age

p5 = Person5("David", 21)
p5b = Person5("Colin", 22)

print(p5.name, p5.age)
print(p5b.name, p5b.age)

###### another example

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

a = Fruit("Apple", 100)
b = Fruit("Banana", 400)
a.color = "Red"         # don't really understand this bit, seems I can pass things that are not expected within the class? 


print(a.name, a.calories, a.color)
print(b.name, b.calories)      

############## PRACTICE QUESTIONS
## 302.08

class Foo:
    def __init__(self, name):
        self.name = name
    
a = Foo("a")
b = Foo("b")
a.name = b.name
b.name = "c"
a.x = 2
b.x = 1
x = (a.x + b.x) * (a.name + b.name)
print(x)                                # bcbcbc

## 302.09 -- create a ContactInformation class

class ContactInformation():
    def __init__(self, first_name, last_name, email, phone_number, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = country

person1 = ContactInformation("fn", "ln", "e", 1234)
person2 = ContactInformation("b", "c", "e", 1234, "FR")

# PE.io example: 

class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = None


person1 = ContactInformation(
    "Joe", "Smith", "JoeSmith@algoexpert.io", "905-999-9999")
person2 = ContactInformation(
    "Sarah", "Jones", "SarahJones@algoexpert.io", "416-333-2134")