## method is a function defined inside a class

## 3 important types of method: 

## instance method, class method, static method 

class Instructor:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.capitalize()

    def say_name(self):
        print(f"My name is {self.name.capitalize()}!")


tim = Instructor("tim")
tim.say_name()

### the following are examples of instance methods

class Person:
    def __init__(self, name):
        self.name = name

    ## to make a method inside a class, you use the def keyword

    def say_hello(self): 
        print(f"hello, {self.name}")

    def set_age(self, age):
        self.age = age

p1 = Person("david")
p1.say_hello()

p1.set_age(41)
print(p1.age)

### 

class Person2:
    def __init__(self, name):
        self.name = name

    ## to make a method inside a class, you use the def keyword

    def say_hello(self): 
        print(f"hello, {self.name}")

    def set_age(self, age):
        self.age = age

    def get_age(self, age):
        return self.age

p2 = Person2("david")
p2.say_hello()

p2.set_age(41)
print(p2.age)
p2.get_age      # this only works if age has already been set, therefore, if you know you might need it later, you should define it as NONE/0 etc: 

class Person3:
    def __init__(self, name):
        self.name = name
        self.age = None         # i'm declaring these as empty for now, so that they can be modified later
        self.weight = None

    ## to make a method inside a class, you use the def keyword

    def say_hello(self): 
        print(f"hello, {self.name}")

    def set_age(self, age):
        self.age = age

    def get_age(self, age):
        return self.age

p3 = Person3("david")
p3.say_hello()

p3.set_age(41)
print(p3.age)
p3.get_age 

##########################################

class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked       # this just toggles the position of the lock

    def count_up(self):
        if self.locked:
            raise Exception("Counter is locked")

        self.count += 1

    def count_down(self):
        if self.locked:
            raise Exception("Counter is locked")

        self.count -= 1

    def print_count(self):
        print(f"the current count is {self.count}")

counter = Counter()
counter.count_up()
counter.print_count()
counter.count_down()
counter.print_count()

counter.toggle_lock()

counter2 = Counter()
counter2.count_up()
counter2.print_count()

counter.count_up()

