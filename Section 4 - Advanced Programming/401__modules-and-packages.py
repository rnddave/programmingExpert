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

