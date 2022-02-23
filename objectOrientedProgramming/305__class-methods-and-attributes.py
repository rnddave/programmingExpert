class Instructor:
    instructors = []

    def __init__(self, name):
        self.name = name
        Instructor.instructors.append(self)


tim = Instructor("Tim")
clement = Instructor("Clement")

print(f"There are {len(Instructor.instructors)} instructors")
for instructor in Instructor.instructors:
    print(f"{instructor.name} is an instructor!")

###############

# class method / attribute, associated to the class only, not the different instances of the class

# class attributes >> 

class Car:

    number_of_cars = 0                  # this is a class attribute
                                        # you might use this count how many instances of the class have been called

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.number_of_cars = 1         # this is an instance attribute
        # but we could keep track of each time it is called
        Car.number_of_cars += 1

print(Car.number_of_cars)               # this is how we call a class attribute

c1 = Car("ford", "edge")
c2 = Car("mazda", "2")

print(c1.number_of_cars)

###########################

# class method >>

class Car2:

    number_of_cars = 0                  # this is a class attribute
                                        # you might use this count how many instances of the class have been called

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.number_of_cars = 1         # this is an instance attribute
        
        Car2.number_of_cars += 1         # this updates the class attribute (not the instance)

    @classmethod                        # this is how we declare a class method
    def update_number_of_cars(cls, cars):
        cls.number_of_cars = cars
        print("run")

Car2.update_number_of_cars(10)

c1b = Car2("ford", "edge")
c2b = Car2("mazda", "2")

print(c1b.number_of_cars)
print(c2b.number_of_cars)

###########################

# another example

class Circle:

    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2* cls.pi * radius

    @classmethod
    def get_area_and_perimieter(cls, radius):
        return cls.area(radius), cls.perimeter(radius)

    # now if we update pi, it updates the class methods
    # these methods are separate from the instances, therefore, corrections or amendments here will affect any instances 
    # important to note that we are grouping similar methods together within the Circle class 

print(Circle.get_area_and_perimieter(4))        # (50.24, 25.12)

####### 305.05 - Employee Class

"""
write a class where each employee has a name, age, salary
should have 2x class attributes to store the average age/salary 
"""

class Employee:

    average_age = 0
    average_salary = 0
    num_emps = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        total_age = Employee.average_age * Employee.num_emps
        total_salary = Employee.average_salary * Employee.num_emps

        Employee.average_age = (total_age + age) / (Employee.num_emps + 1)
        Employee.average_salary = (total_salary + salary) / (Employee.num_emps + 1)
        
        Employee.num_emps += 1

#### 305.06 - Temperature Class

"""
create a temperature class
all instances to contain a KELVIN attribute

2x class attribute: 
min_temperature
max_temperature

these can be modified by calling class methods: 
update_min_temperature
updatemax_temperature

min_temp must always be less than max_temp

each instance, kelvin attribute must be between min & max (inclusively)

"""

class Temperature:
    min_temperature = 0
    max_temperature = 1000

    def __init__(self, kelvin):
        if kelvin > self.max_temperature or kelvin < self.min_temperature:
            raise Exception("Invalid temperature.")

        self.kelvin = kelvin

    @classmethod
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.max_temperature:
            raise Exception("Invalid temperature.")

        cls.min_temperature = kelvin

    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin < cls.min_temperature:
            raise Exception("Invalid temperature.")

        cls.max_temperature = kelvin