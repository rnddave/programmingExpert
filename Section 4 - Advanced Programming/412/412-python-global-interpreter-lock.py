"""
PYTHON GLOBAL INTERPRETER LOCK

- design decision about python architecture
- unique amongs other programming languages


MUTEX

- mutually exclusive lock
- controls access to a section of code
- typically used in multi-threaded programs when a section of code should only execute one thread at a time 
- if a thread has the [mutex] all other threads must wait for it to finish 

"""

"""
video notes

- specific to python 
- cannot create parallel programs in python

- global interpreter 
-- most programming languages allow multiple access to the global interpreter ( or possible multiple interpreters )

- software related thing, a kick-back to the python architecture


WHY? 

- efficiency / speed
- simplicity
- how python handles memory and objects

MEMORY and OBJECTS
- program has an allocation of space in RAM
-- that RAM holds code, variables, etc 

- if multi threads run in parallel, then they can modify the same objects in the same space of memory at the same time 
- this can create inconsistant data 

- to fix this problem, python implemented the global interpreter lock 

- BUT THERE ARE OTHER WAYS TO DO THIS 
-- other programming languages lock the code using mutex
-- but each time the lock is placed or unlocked, etc, it slows down the interpreter 
-- makes the other programming languages more complicated etc

Python & C
- lots of C programmes running behind the scenses in python
- global interpreter lock allows these to run efficiently

REFERENCE COUNT
- like a garbage collector
- something to reference what we've been using in memory
- a way of clearing un-needed memory objects
-- e.g. create variable = reference count of +1 delete a variable and reference count -1 etc 


"""