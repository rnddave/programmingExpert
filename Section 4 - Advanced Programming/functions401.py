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