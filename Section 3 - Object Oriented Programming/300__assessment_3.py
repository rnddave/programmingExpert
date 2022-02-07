"""
Geometry inheritance

create 4x class [Polygon], [Triangle], [Rectangle], [Square]

The [Triangle] and [Rectangle] class should be subclasses of [Polygon] and [Square] should be a subclass of [Rectagle] 

Your [Polygon] class should raise a [NotimplementedError] when the [get_area()] and [get_sides()] methods are called. 
However it should correctly return the perimeter of the polygon when [get_perimeter()] is called. Treat [Polygon] class as an *abstract* class. 

Your [Triangle] class should have a constructor that takes 3 arguments, which will be the len of the 3x side. 
You may assume that the sides passed will always for a triangle. 

Your [Rectangle] class should have a constructor that takes 2 arguments, which will be the [width] and [height] of the [Rectangle]

Your [Square] class should have a constructor that takes 1 argument which will be the length of each side of the [Square]

Your [Triange] and [Rectangle] classes should both implement the following methods: 
-- [get_sides()] = return a list containing the lengths of the sides of the shape
-- [get_area()] = area of the polygon

Your [Square] class should only have an implementation for its constructor, and rely on the [Rectangle] superclass for implementations of [get_sides()] and [get_area()]

"""

import math

class Polygon:
    def get_sides(self):
        # Your [Polygon] class should raise a [NotimplementedError] when the [get_sides()] methods are called.
        raise NotImplementedError

    def get_area(self):
        # Your [Polygon] class should raise a [NotimplementedError] when the [get_area()] methods are called.
        raise NotImplementedError

    def get_perimeter(self):
        return sum(self.get_sides())

class Triangle(Polygon):
    # Your [Triangle] class should have a constructor that takes 3 arguments, which will be the len of the 3x side. 
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    def get_sides(self):
        return self.sides

    def get_area(self):
        side1, side2, side3 = self.sides
        return get_triangle_area(side1, side2, side3)

"""
Your [Triange] and [Rectangle] classes should both implement the following methods: 
-- [get_sides()] = return a list containing the lengths of the sides of the shape
-- [get_area()] = area of the polygon
"""

class Rectangle(Polygon):
    # Your [Rectangle] class should have a constructor that takes 2 arguments, which will be the [width] and [height] of the [Rectangle]
    def __init__(self, width, height):
        self.width = width
        self.height = height  

    def get_sides(self):
        return [self.width, self.height, self.width, self.height]
        # we need to duplicate  height/width as we know there are 4 sides, so take in 2 sides and then duplicate (this is used again in square)

    def get_area(self):
        return get_rectangle_area(self.width, self.height)
"""
Your [Triange] and [Rectangle] classes should both implement the following methods: 
-- [get_sides()] = return a list containing the lengths of the sides of the shape
-- [get_area()] = area of the polygon
"""

class Square(Rectangle):
    # Your [Square] class should have a constructor that takes 1 argument which will be the length of each side of the [Square]
    def __init__(self, length):
        # Your [Square] class should only have an implementation for its constructor, and rely on the [Rectangle] superclass for implementations of [get_sides()] and [get_area()]
        super().__init__(length, length)
        # what we see here, is that we will pass 2x measurement to the method in Rectangle, that will correspond with the 2x arguments it expects (height, width)
        # we know a square is the same on all sides, however, by passing the same measurement, duplicated, to existing code, we can use that code to perform the math


    # Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


    # Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height
