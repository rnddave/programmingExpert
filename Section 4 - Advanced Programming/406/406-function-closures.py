"""
Function Closures >>

tricky subject

"""

def outer(x, y):
    def nested():
        return x + y

    return nested

value = outer(1, 2)()
print(value)

"""
OUTPUT >> 


"""