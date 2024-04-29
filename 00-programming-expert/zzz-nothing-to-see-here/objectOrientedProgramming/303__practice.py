## 303.01 - Rectangle class: 

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

## add following methods to Rectangle class:
# change_position(), accept 2 parameters (x,y) it should set corresponding instance attributes such that they are equal to arguments passed

# get_position() should return the position of the rectangle as a tuple (x, y)

# get_area() should return the area of the rectangle based on instance attributes

    def change_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.pos = (new_x, new_y)

    def get_position(self):
        return self.x, self.y

    def get_area(self):
        return self.width * self.height


## 303.02 - Group class: 

class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    # # add following methods: 
    # add() accept name as a parameter and adds to group 
    # delete() accept name as parameter and remove from group, but if no name in group, then raise exception
    # get_members() return a sorted list

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group")


    def get_members(self):
        return sorted(self.members)

## 303.03 - Group Class - part 2

class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)

    # add a new method called merge()
    # merge() should accept as a parameter the instance of another Group object, 
    # then merge the 2 groups and return a new group, listing all members from both groups 

    def merge(self, groupY):
        combined_members = self.members + groupY.members
        new_group = Group("", combined_members)
        return new_group



