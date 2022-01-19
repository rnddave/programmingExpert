### ABSTRACT CLASSES

"""
This is a difficult topic
"""

class AbstractVehicle:
    def get_max_speed(self):
        raise NotImplementedError

    def get_make(self):
        raise NotImplementedError

    def get_wheel_count(self):
        raise NotImplementedError

    def display(self):
        print(f"Make = {self.get_make()}, Wheel Count = {self.get_wheel_count()}, Top Speed = {self.get_max_speed()}")


class Car(AbstractVehicle):
    def __init__(self, make):
        self.make = make

    def get_wheel_count(self):
        return 4

    def get_make(self):
        return self.make


class Motorcycle(AbstractVehicle):
    def __init__(self, make):
        self.make = make

    def get_wheel_count(self):
        return 2

    def get_make(self):
        return self.make


class Tesla(Car):
    def __init__(self, model):
        super().__init__("Tesla")
        self.model = model

    def get_max_speed(self):
        if self.model == "Plaid":
            return 250
        return 200


class Yamaha(Motorcycle):
    def __init__(self):
        super().__init__("Yamaha")

    def get_max_speed(self):
        return 150


vehicles = [Tesla("Plaid"), Yamaha(), Tesla("S")]
for vehicle in vehicles:
    vehicle.display()

###########################

## ABSTRACT METHOD

"""
A method that is defined in an interface or abstract class and does not provide an implementation. 

Designed to be overridden by BASE or SUBCLASSES that extend the class or implement the interface they are defined in 
"""

## ABSTRACT CLASS

"""
A Class that contains at least one abstract METHOD and is not meant to be instantiated.

Abstract CLASSES are menat to act as the parent or base class in an inheritance hierachy. 
Typically abstract classes implement some functionality that can be used commonly by all child/subclasses
"""

#############################

"""
FRoM THE VIDEO

Abstract class should not have any instances of it 
the purpose is to increase abstraction of the program 
classes that never have any instance of themselves, but they are used to populate other classes 

AN ABSTRACT METHOD = means that any class that takes from the abstract class must also take that method

#################

Interestingly, in Python, there is no notion of ABSTRACT CLASS, we define it no differently, we just use it differently 
we follow the rules by convention, not by force 

ABSTRACT = GENREAL (Abstraction = Generalise) 

"""
import random

class AbstractGame:     # NB the name - AbstractX - this is not required, this just reminds other we WANT this to be an abstract class (do not instantiate)
    
    def start(self):
        while True:
            start = input("would you like to play?")
            if start.lower() == "yes":
                break

        self.play()

    def end(self):
        print("The game has ended.")
        self.reset()

    def play(self):
        raise NotImplementedError("You must provide an implementation for play()")     # this is used to note that anything that derives from this class, should implement own method (???)

    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset()")      
                                                                                        # whenever you see this NoImplementedError, it is likely to be an abstract class/method

class RandomGuesser(AbstractGame):
    def __init__(self, rounds):
        self.rounds = rounds
        self.round = 0

    def reset(self): 
        self.round = 0 

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}. let's begin!")
            randum_num = random.randint(0, 9)

            while True:
                guess = input("Enter a number between 1-10: ")
                if(guess) == randum_num:
                    print("You got it!")
                    break
        
        self.end()

class AnotherGame(AbstractGame):
    pass

games = [RandomGuesser(2), AnotherGame()]

for game in games:
    game.start()
                
"""
non-abstract classes are also called 'concerete classes'

if we had a bunch of different games, we don't need to know anything about them, we just call the start and see what happens
"""
