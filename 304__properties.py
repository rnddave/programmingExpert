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

tim.name = 13  # this should raise an exception!

######################

