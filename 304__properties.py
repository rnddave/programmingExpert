class Instructor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name.capitalize()

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise Exception("Name must be a string!")

        if len(value) == 0:
            raise Exception("Name cannot be empty!")

        self._name = value


tim = Instructor("tim")
print("Capitalized name:", tim.name)

tim.name = "timothy"
print("Capitalized name:", tim.name)

#tim.name = 13  # this should raise an exception!

######################

## tip = make sure your class names are useful, it should be the collection of instances
## probably don't want to name classes as plural as an example, each instance of the class is a separate instance

# properties are special attributes 

class Person:
    def __init__(self, name): 
        self.name = name
        self.salary = 0

p = Person("Tim")
p.salary = -100     # now there is nothing stopping me from doing this, but it would be unusual for someone to have a negative salary, so we want to block this

class Person2:
    def __init__(self, name): 
        self.name = name
        self._salary = 0    # this UNDERSCORE denotes that it 'should' be private, but it isn't really locked, we rely on people to follow the rules
                            # this says 'it's a private attribute, you should not change it' - YOU CAN CHANGE IT, you just shouldn't

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Hey, this isn't really a good number for this input")
        self._salary = salary

    def get_salary(self):
        return round(self._salary)

    # creating a property (LEGACY WAY)

    salary = property(get_salary, set_salary)   

p = Person2("Tim")
p.salary = 100.99

print(p.salary)

class Person3:
    def __init__(self, name): 
        self.name = name
        self._salary = 0    # this UNDERSCORE denotes that it 'should' be private, but it isn't really locked, we rely on people to follow the rules
                            # this says 'it's a private attribute, you should not change it' - YOU CAN CHANGE IT, you just shouldn't

    @property               # creating a property (NEW / preferred WAY)
    def salary(self):
        return round(self._salary)
    
    @salary.setter          # another property
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Hey, this isn't really a good number for this input")
        self._salary = salary

    # THIS IS THE OLD WAY OF SETTING PROPERTIES
    # # salary = property(get_salary, set_salary)   

p = Person3("Tim")
p.salary = 103.99

print(p.salary)

#####################

class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        print("run")
        return self._second

    @second.setter
    def second(self, second): 
        if second < 0 or second > 60:
            raise ValueError("Invalid")
        self._second = second
    
t = Time(54)
t.second = 59
print(t.second)
print("\n\n\n\n\n\n\n")

#######################

## 304.04 - Bank Account Class
"""
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name

we need to add a private attribute named [balance] and implement a getter/setter for it

for this question, do not use @property decorator (use the legacy option)

Balance constraints: 

bal >= 0
bal <= 100,000
bal must be a number
bal to round to nearest $

"""

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def set_balance(self, balance):
        if type(balance) not in [int, float]:
            return

        if balance < 0 or balance >= 100000:
            return
        
        self._balance = balance

    def get_balance(self):
        return round(self._balance)

    
## 304.05 - Bank Account Class - part 2
"""
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name

we need to add a private attribute named [balance] and implement a getter/setter for it

for this question, do use @property decorator (do not use the legacy option)

Balance constraints: 

bal >= 0
bal <= 100,000
bal must be a number
bal to round to nearest $

"""

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, balance):
        if type(balance) not in [int, float]:
            return

        if balance < 0 or balance > 100000:
            return
        
        self._balance = balance

