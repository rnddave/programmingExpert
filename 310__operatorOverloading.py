#### OPERATOR OVERLOADING 
"""
Dunder Method

Dunder Methods are methods that are prefixed and suffixed by 2 underscores

The most important is the __init__ that we have seen many times already 
Sometimes this is known as the CONSTRUCTOR of the CLASS and defines how a new instance is initialized after being created

Implementing those methods will sometimes change how certain operators will behave
like + with __add__ and == with __eq__. 

Other examples include __len__, __str__, __repr__
"""
## Example Code: 

class Menu:
    def __init__(self, items):
        # Note that since the MenuItem has a __gt__ dunder method overridden,
        # the sorting will by default sort the items by name.
        self.items = sorted(items)

    def __str__(self):
        s = f"*** Menu ({len(self)} items) ***\n"
        for item in self.items:
            s += f"- {item.name}: ${item.price} ({item.calories} calories)\n"
        return s

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Menu(self.items + other.items)


class MenuItem:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __eq__(self, other):
        return (self.name, self.price, self.calories) == (other.name, other.price, other.calories)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.name > other.name


items1 = [
    MenuItem("Apple", 1, 50),
    MenuItem("Filet Mignon", 10, 500),
    MenuItem("Cake", 5, 350),
    MenuItem("Zucchini", 3, 15),
    MenuItem("Wine", 30, 250),
]
menu1 = Menu(items1)
print(menu1)

items2 = [
    MenuItem("Orange", 1, 50),
    MenuItem("Pasta", 8, 300),
    MenuItem("Beef", 10, 500),
]
menu2 = Menu(items2)
print(menu2)

print(menu1 + menu2)
########## VIDEO TIME 
"""
operator overload = ability to implement custom implentations on our own classes

"""

## __add__ (addition)

class Page:
    def __init__(self, words, page_number):
        self.words = words
        self.page_number = page_number

    def __add__(self, other):           # dunder method = duoble underscore method
                                        # (self, other) == basically read as "left operand", "right operand"
        new_words = self.words + " " + other.words
        new_page_number = max(self.page_number , other.page_number) + 1
        return Page(new_words, new_page_number)

page1 = Page("PAGE ONE", 1)
page2 = Page("PAGE TWO", 2)
page3  = page1 + page2
print(page3.words, page3.page_number)

## __sub__ (subtraction)

class StoreItem:
    TAX = 0.13

    def __init__(self, name, price):
        self.name = name
        self.price = price 
        self.after_tax_price = 0
        self.set_after_tax_price()

    def set_after_tax_price(self):
        self.after_tax_price = round(self.price * (1+ self.TAX), 2)

    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)

bread = StoreItem("Bread", 7)
discounted_bread = bread - 2
print(discounted_bread.after_tax_price)

## __mul__ (multiplication)

class StoreItem:
    TAX = 0.13

    def __init__(self, name, price):
        self.name = name
        self.price = price 
        self.after_tax_price = 0
        self.set_after_tax_price()

    def set_after_tax_price(self):
        self.after_tax_price = round(self.price * (1+ self.TAX), 2)

    def __sub__(self, discount):
        return StoreItem(self.name, self.price - discount)

    def __mul__(self, value):
        return StoreItem(self.name, self.price * value)

bread = StoreItem("Bread", 7)
discounted_bread = bread - 2
print(discounted_bread.after_tax_price)
discounted_bread = bread * 0.8
print(discounted_bread.after_tax_price)

## __trudiv__  & __floordiv__ (division)

class Line: 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __truediv__(self, factor):       # truediv = regular division = /
        new_point1 = (self.point1[0] / factor, self.point1[1] / factor)
        new_point2 = (self.point2[0] / factor, self.point2[1] / factor)
        return Line(new_point1, new_point2)

line1 = Line((10, 5), (20, 10))
line2 = line1 / 2
print(line2.point1, line2.point2)

# ---

class Line: 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __floordiv__(self, factor):       # floordiv = integer division = // [ basically rounding up ]
        new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
        new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
        return Line(new_point1, new_point2)

line1 = Line((10, 5), (20, 9))
line2 = line1 // 2
print(line2.point1, line2.point2)
        
## __len__ (length)

import math

class Line: 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __floordiv__(self, factor):       # floordiv = integer division = // [ basically rounding up ]
        new_point1 = (self.point1[0] // factor, self.point1[1] // factor)
        new_point2 = (self.point2[0] // factor, self.point2[1] // factor)
        return Line(new_point1, new_point2)

    def __len__(self):
        distance_x = (self.point1[0] - self.point2[0]) ** 2
        distance_y = (self.point1[1] - self.point2[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)

line1 = Line((10, 5), (20, 10))
line2 = line1 // 2
print(line2.point1, line2.point2)
print(len(line1))

## __eq__ & __ne__ (equality comparison)

class Line: 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __len__(self):
        distance_x = (self.point1[0] - self.point2[0]) ** 2
        distance_y = (self.point1[1] - self.point2[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)

line1 = Line((10, 5), (20, 10))
line2 = Line((10, 5), (20, 10))
print(line1 == line2)           # False [ this is because although have same values, they are different objects]
                                # because we actually do want to compare the values, rather than the objects.

################## SO LETS FIX THIS >>>>>>>>>>>>>>>>>>>>>>>>>>>

class Line: 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __len__(self):
        distance_x = (self.point1[0] - self.point2[0]) ** 2
        distance_y = (self.point1[1] - self.point2[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)

    def __eq__(self, other):           ## equals
        if not isinstance(other, Line):
            return False

        return self.point1 == other.point1 and self.point2 == other.point2

    def __ne__(self, other):           ## not equals
        return not self.__eq__(other)

line1 = Line((10, 5), (20, 10))
line2 = Line((10, 5), (20, 10))
line3 = Line((10, 4), (22, 10))
print(line1 == line2)                   # True
print(line3 != line2)                   # True

## __gt__ & __lt__ (other comparison)

class Line: 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __len__(self):
        distance_x = (self.point1[0] - self.point2[0]) ** 2
        distance_y = (self.point1[1] - self.point2[1]) ** 2
        distance = math.sqrt(distance_x + distance_y)
        return round(distance)

    def __eq__(self, other):           ## equals
        if not isinstance(other, Line):
            return False

        return self.point1 == other.point1 and self.point2 == other.point2

    def __ne__(self, other):           ## not equals
        return not self.__eq__(other)

    def __gt__(self, other):            # greater than
        return len(self) > len(other)

    def __ge__(self, other):            # greater than OR equal to       
        return len(self) >= len(other)

    def __lt__(self, other):            # less than   
        return len(self) < len(other)

    def __le__(self, other):            # less than OR equal to
        return len(self) <= len(other)

line1 = Line((10, 5), (20, 10))
line2 = Line((10, 5), (20, 10))
line3 = Line((10, 4), (22, 10))

print(line1 > line3)                # False
print(line2 < line3)                # True

## __str__ & __repr__ (string() & repr())

class Page:
    def __init__(self, text, page_number):
        self.text = text
        self.page_number = page_number

    def __len__(self):
        return len(self.text)

    def __str__(self):
        return f"Page({self.text}, {self.page_number})"

    def __repr__(self):         # outputs the machine representation of an object (useful for debugging)
        return self.__str__()

class Book:
    def __init__(self, title, author, pages, id_number):
        self.title = title
        self.author = author
        self.pages = pages
        self.id_number = id_number

    def __len__(self):
        return len(self.pages)

    def __str__(self):
        output = f"Book({self.title}, {self.author}, {self.id_number})"

        for page in self.pages:
            output += "\n" + str(page)

        return output

    def __repr__(self):         # outputs the machine representation of an object (useful for debugging)
        return f"Book({self.id_number})"

###>>>#####>>>>#####>>>

page1 = Page("Page ONE", 1)
page2 = Page("The second page", 2)
book = Book("the best book", "Tim", [page1, page2], 1)
print(page1, page2)
print(book)

##### looking at the repr

print(repr(book))       # Book(1)
print(repr(page1))      # Page(Page ONE, 1)

###################### TIME FOR PRACTICE ######################

## 310.05 >> VECTOR CLASS
"""
write a vector class that implements: 

__init__(self, a, b)

__eq__(self, vector) [returns TRUE if current vector and the vector parameter are equal]

__repr__(self) [return the string representation of the vector]

__add__(self, vector) [create and return a new vector object that has components equal to the sum of the components 
in the current vector and the vector represented by the vector parameter]

__sub__(self, vector) [create and return a new vector object that has components equal to the difference of the components 
in the current vector and the vector represented by the vector parameter]

__mul__(self, vector) [returns the dot product of the current vector and the vector represented by the vector parameter
the dot product of two vectors is equal to the sum of the multiplication of their individual components]
"""

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b

    def __repr__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, vector):
        new_a = self.a + vector.a
        new_b = self.b + vector.b
        return Vector(new_a, new_b)

    def __sub__(self, vector):
        new_a = self.a - vector.a
        new_b = self.b - vector.b
        return Vector(new_a, new_b)

    def __mul__(self, vector):
        return self.a * vector.a + self.b * vector.b