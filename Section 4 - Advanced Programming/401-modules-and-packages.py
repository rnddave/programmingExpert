"""
Modules & Packages (Files & Folders)

Main Module
- in python = run or invoked directly
- auto set the __name__ variable to the string "__main__"

Module
- simply any Python file (end in .py)
- split the code into multiple files
- make programs easier to understand
- abilty to import from one to another

Package
- directoy containing special named __init__.py
- typically a collection of other python modules
- provides a way to organise python modules
"""
#---------------------------------------------------------

def main(name):
    print(f"Hello {name}!")


if __name__ == "__main__":
    main("ProgrammingExpert")

#---------------------------------------------------------

"""
Video details

Main Module is the program that is run 

to check; __name__
"""
print(__name__) # __main__

#---------------------------------------------------------

import functions401

functions401.bar()
print("run")

#---------------------------------------------------------

# you can also rename at import: 

import functions401 as f401

f401.foo()

t = f401.Test()
print(t)

#---------------------------------------------------------

# you could also import the actual methods/functions/class from the module at import,
#  therefore not needing to refer to the module name

from functions401 import foo, bar, Test     # if you use from XX import *
                                            # (the asterix) this allows you to import everything from a module (bad-practice)

bar()   # allowing us to call it without the module name anylonger
foo()

#---------------------------------------------------------

def func():
    print("func")

#---------------------------------------------------------

"""

you can import other modules into this module as well, however, 
you cannot create circular references (import from X to Y and from Y to X)
-- this would create an infinte loop causing import to import itself

a common practice is to have one module that imports all the other modules, then you just need to import a single module

"""

#---------------------------------------------------------

"""

sometimes you want to run code in the module, but not when it is imported

you need additional code: 

if __name__ == "__main__":
    print("hello world")

"""

#---------------------------------------------------------

if __name__ == "__main__":
    print("hello world (from main)")

#---------------------------------------------------------

"""

let's import a whole package: 

first we need to create a§ directory, within the directory, we need to create a file called 

__init__.py

"""

#---------------------------------------------------------

import code401
                # output as follows:
                # A
                # B


