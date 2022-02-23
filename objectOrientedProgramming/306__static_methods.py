## static methods

"""
a static method is defined whithin a class but should not reference anything relevant to that class specifically except for other static methods

mostly used for PURE functions which do not use temp variables outside of their own scope and exclusively transform a set of inputs into some outputs

for instance a method that converts a distance from a KM to MILE should most likely be static 

denoted using @staticmethod
"""

import math


class Geometry:
    @staticmethod
    def perimeter_of_square(side_length):
        return 4 * side_length

    @staticmethod
    def area_of_square(side_length):
        return side_length ** 2

    @staticmethod
    def perimeter_of_circle(radius):
        return 2 * math.pi * radius

    @staticmethod
    def area_of_circle(radius):
        return math.pi * (radius ** 2)


print("Perimeter of square with side of length 7:", Geometry.perimeter_of_square(7))
print("Area of square with side of length 7:", Geometry.area_of_square(7))

print("Perimeter of circle with radius of length 3:", Geometry.perimeter_of_circle(3))
print("Perimeter of circle with radius of length 3:", Geometry.area_of_circle(3))

#################

"""
really a method that sits inside a class, but doesn't have access to the [cls] or [self] 

usually highly related to that class

"""

class Student: 
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades 

    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades)

s1 = Student("David", [80, 59, 65, 79])
s2 = Student("Xiao", [100, 56, 78, 90])

average = s1.average_from_grades(s1.grades)
print(average)
average = s1.average_from_grades(s2.grades)
print(average)
average = s1.average_from_grades(s1.grades[:2])
print(average)
average = s1.average_from_grades(s1.grades + s2.grades)
print(average)

#############################
# Static Attributes = class attributes = same in python 

#############################

class Student2: 
    grade_bump = 2.0                                    # class attribute (or static attribute)
    
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades 

    def average(self):                                  # Instance Method
        return sum(self.grades) / len(self.grades)

    @classmethod                                        # Class Method 
    def average_from_grades_plus_bump(cls, grades):
        average = cls.average_from_grades(grades)
        return min(average + cls.grade_bump, 100)
    
    @staticmethod                                       # Static Method
    def average_from_grades(grades):
        return sum(grades) / len(grades)


"""
main difference a class method can access anything else about the class

a static method should act like a function, it should not rely on anything else, work independent of anything else
technically you can do it, but it is bad practice 
"""

######################################

### 306.03 - Pysics Class

"""
create a [Pyhsics] class

contain no constructor method and three static method as outline below: 

[calculate_net_force] = return product of [mass] and [acceleration]
[calculate_acceleration] = return the quotient of [net_force] and [mass]
[calculate_mass] = return the quotient of [net_force] and [acceleration]

"""

class Physics:

    @staticmethod
    def calculate_net_force(mass, acceleration):
        
        if mass < 0 or acceleration < 0:
            return 0.0

        return mass * acceleration

    @staticmethod
    def calculate_acceleration(mass, net_force):
        
        if net_force < 0 or mass <= 0:
            return 0.0

        return net_force / mass

    @staticmethod
    def calculate_mass(net_force, acceleration):

        if net_force < 0 or acceleration <= 0:
            return 0.0

        return net_force / acceleration