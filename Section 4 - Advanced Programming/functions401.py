"""
This file is supporting the concept of multiple modules for the 401 class material
"""

def foo():
    print("foo")

def bar():
    print("bar")

class Test:
    pass


"""

you can import other modules into this module as well, however, 
you cannot create circular references (import from X to Y and from Y to X)
-- this would create an infinte loop causing import to import itself

"""

#---------------------------------------------------------

"""

sometimes you want to run code in the module, but not when it is imported

you need additional code: 

if __name__ == "__main__":
    print("hello world")

this code basically prevents this part from being imported, but if in this module, you can run the code

"""

#---------------------------------------------------------

if __name__ == "__main__":
    print("hello world (from function)")