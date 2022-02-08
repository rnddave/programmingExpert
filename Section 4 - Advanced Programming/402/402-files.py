"""
Files

The ability to handle file is essential, python has you covered

"""

with open("402-awesome_people.txt", "w") as file:
    file.write("Tim\n")
    file.write("Antoine\n")
    file.write("Clement")

file = open("402-awesome_people.txt", "r")
awesome_people = file.read().split("\n")
file.close()

print(awesome_people)