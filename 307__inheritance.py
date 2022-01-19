## Inheritance

class Animal:
    def __init__(self, species):
        self.species = species


class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def speak(self):
        print(f"{self.species} named {self.name}: Woof!")


class Cat(Animal):
    def __init__(self, age):
        super().__init__("Cat")
        self.age = age

    def speak(self):
        print(f"{self.age} year old {self.species}: Miao!")


animals = [Dog("Rex"), Cat(13), Dog("Rose")]
for animal in animals:
    animal.speak()

"""
>> Parent / Child <<
when a class [a] inherits from [b], we say [a] is a child of [b] 

when a class [c] inherits from [d], we say that [d] is a parent of [c]

>> POLYMORPHISM << 
this is a term originating from biology, where a poly means many and morphism means forms. 
But in programming it means an object behaving in different ways depending on the contect it is used in 

>> Mehot overriding << 
when a programmer redefines a method on a class that was already defined in it's parent class
"""

## very important OOP concept 

"""
Employee        = a Person
Manager         = a Person + Employee 
Owner           = Person 

"""

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def say_hello(self): 
        print(f"Hi my name is {self.firstname} {self.lastname}")

class Employee(Person):         # you can pass multiple classes
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary
  
    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary}")
    
    def test(self):
        print("test")

e = Person("David", "D")
e.say_hello()                   # Hi my name is David D

f = Employee("Xiao", "w", 56000)
f.say_hello()                   # Hi my name is Xiao w
                                # My salary is 56000

#####################################################

"""
Person          = a Person
Employee        = a Person
Manager         = a Person + Employee 
Owner           = a Person 

"""

## OTHER Inheritence OR MULTIPLE Ineritence

class Person2:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def say_hello(self): 
        print(f"Hi my name is {self.firstname} {self.lastname}")

class Employee2(Person2):         # you can pass multiple classes
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary
  
    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary}")
    
class Manager(Employee2):
    def __init__(self, firstname, lastname, salary, department):
        super().__init__(firstname, lastname, salary)
        self.department = department

class Owner(Person2):
    def __init__(self, firstname, lastname, net_worth):
        super().__init__(firstname, lastname)
        self.net_worth = net_worth
    
e = Person2("David 2", "D")
e.say_hello()                       # Hi my name is David D
print(type(e))                      # <class '__main__.Person2'>

f = Employee2("Xiao 2", "w", 56000)
f.say_hello()                       # Hi my name is Xiao w
                                    # My salary is 56000
print(type(f))                      # <class '__main__.Employee2'>

m = Manager("Tim", "L", 85000, "bossman")
m.say_hello()
print(type(m))                      # <class '__main__.Manager'>

o = Owner("John", "Franklin", 1000000)
o.say_hello()
print(type(o))                      # <class '__main__.Owner'>
print(isinstance(o, Person2))       # True

################################

## multiple inheritence

"""
this, in python, differs from other programming languages

it can be complex, but is rarely used, however, is interesting when used correctly
"""

class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A, B):                      # we go through these classes in order they are defined
    pass

c = C()                             # output == A

class A2:
    def __init__(self):
        print("A")

class B2:
    def __init__(self):
        print("B")

class C2(A2, B2):                      # we go through these classes in order they are defined
    def __init__(self):
        super().__init__()

c2 = C2()                             # output == A

"""
MRO = Method Resolution Order

the order in which methods are evaluated against

if not in main class, then look in second super class, then third super class, etc
"""

###################

## Duck Typing

"""
if it walks like a duck, flys like a duck, it must be a duck

basically, this is an example of looking at how python will allow a program to compile and only fails when the faulty code is reached
"""

class Duck: 
    def swim(self):
        print("swimming duck")

    def fly(self):
        print("flying duck")

class Whale: 
    def swim(self):
        print("swimming whale")

animals = [Duck(), Duck(), Whale()]

for animal in animals:
    animal.swim()
    # animal.fly()          = this is the Duck typing, python assumes it will be able to run because it looks syntactically correct, until it tries to run it

    """
    >>>> OUTPUT <<<<

swimming duck
flying duck
swimming duck
flying duck
swimming whale

Traceback (most recent call last):
  File "/Users/dickinsd/Github/programmingExpert/307__inheritance.py", line 201, in <module>
    animal.fly()
AttributeError: 'Whale' object has no attribute 'fly'
    
    """

############ PRACTICE ###########

## 307.7 - Animal Inheritance
"""
create an Animal, Mammal, Reptile class as defined: 

- All Animals have an AGE, WEIGHT, HEIGHT
- All Mamals have a SEX
- Most reptiels have 4 LEGS (but not all)

Then create a Monkey, Lizard class that inherrit from proper base class

- MONKEY = 5 FINGERS and COLOR
- LIZARD = TAIL and COLOR
"""

class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height


class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        super().__init__(age, weight, height)
        self.sex = sex


class Reptile(Animal):
    def __init__(self, age, weight, height, legs):
        super().__init__(age, weight, height)
        self.legs = legs


class Monkey(Mammal):
    fingers = 5

    def __init__(self, age, weight, height, sex, color):
        super().__init__(age, weight, height, sex)
        self.color = color


class Lizard(Reptile):
    tail = True

    def __init__(self, age, weight, height, legs, color):
        super().__init__(age, weight, height, legs)
        self.color = color