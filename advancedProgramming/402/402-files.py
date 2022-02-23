"""
Files

The ability to handle file is essential, python has you covered

"""

with open("402-awesome_people.txt", "w") as file:   # the default location is the location you are currently when you run the python program
                                                    # the 'as file' opens the file as the variable 'file'
    file.write("Tim\n")
    file.write("Antoine\n")
    file.write("Clement")

# open("402-awesome_people.txt", "w") - WARNING!!! -
# IF THE FILE ALREADY EXISTS, THE FILE WILL BE EREASED and RECREATED = THIS IS NOT AN APPEND or AMEND 

# -=-=-=-=-=-=-=-=-=-=-=-=-

file = open("402-awesome_people.txt", "r")          # this is how to open an existing file
awesome_people = file.read().split("\n")            # file.read() = read all of the text as a large string
                                                    # with the \n break word = new line character

file.close()                                        # close the file, to save resources etc

print(awesome_people)
print(type(awesome_people))                         # <class 'list'>

# can also use the .strip() to remove white space: 

file = open("402-awesome_people.txt", "r")      
awesome_people2 = file.read().strip()    

print(awesome_people2)                              # Tim
                                                    # Antoine
                                                    # Clement
print(type(awesome_people2))                        # <class 'str'>

file.close()                                        # close the file, to save resources etc

# -=-=-=-=-=-=-=-=-=-=-=-=-

# open("402-awesome_people.txt", "w") - WARNING!!! -
# IF THE FILE ALREADY EXISTS, THE FILE WILL BE EREASED and RECREATED = THIS IS NOT AN APPEND or AMEND 

# so we can use the APPEND operator to add to the end of the file:
#  [ >> we can use the \n to add a new line after each entry <<]

with open("402-awesome_people.txt", "a") as file:
    file.write("Blah\n")
    file.write("Blah2\n")
    file.write("Blah3")

file = open("402-awesome_people.txt", "r")      
awesome_people3 = file.read().strip()    

print(awesome_people3)                              # Tim
                                                    # Antoine
                                                    # Clement    
                                                    # Blah
                                                    # Blah2
                                                    # Blah3         
                                                    

file.close()                                        # close the file, to save resources etc

# -=-=-=-=-=-=-=-=-=-=-=-=-

# r+ ===== Read & Write:
#  [ >> we can use the \n to add a new line after each entry <<]

with open("402-awesome_people4.txt", "r+") as file:
    file.write("\n\nfile4\n")
    file.write("Blah2\n")
    file.write("Blah3")

file = open("402-awesome_people4.txt", "r")      
awesome_people4 = file.read().strip()    

print(awesome_people4)                              # file4
                                                    # Blah2
                                                    # Blah3   

file.close()                                        # close the file, to save resources etc
# -=-=-=-=-=-=-=-=-=-=-=-=-

# r+ ===== Read & Write:
# in reality, you want to update the file rather than write over the file as follows:

with open("402-scores.txt", "w") as file:           # first we will create a file with some starting data
    file.write("\n\nSCORES\n")
    file.write("5\n")
    file.write("6")

file.close()                                        # close the file, to save resources etc

with open("402-scores.txt", "r+") as file:
    score = file.read()
    print(score)
    file.write("\n7")    

with open("402-scores.txt", "r") as file:
    score2 = file.read()
    print(score2)

"""
we can use .seek() to find locations in the file, to write other existing material for example: 

file.seek(0)        << the start of the file
file.seek(1)        << set the reference point where the curser is (???)
file.seek(2)        << set to the end of the file 

"""

# now we can consider iterating through the file:
# option 1 >> using the index >>

with open("402-awesome_people5.txt", "r+") as file:
    lines = file.readlines()[:3]

# now we can consider iterating through the file:
# option 2 >> for loop (for line in file) >>

with open("402-awesome_people5.txt", "r+") as file:
    for line in file:
        print(line, end="")


print("\n\n")

# but what if I only wanted first 3 lines?
# option 2 >> using a COUNT >> for loop (for line in file) >>

with open("402-awesome_people5.txt", "r+") as file:
    count = 0
    for line in file:
        print(line, end="")
        count += 1
        if count >= 3:
            break

print("\n\n")

# better to use enumerate
# option 3 >> using a enumerate >> for loop (for line in file) >>

with open("402-awesome_people5.txt", "r+") as file:
    for i, line in enumerate(file):
        print(line, end="")
        if i == 2:
            break

file.close()                                        # close the file, to save resources etc
print("\n\n")
# -=-=-=-=-=-=-=-=-=-=-=-=-

# reading files by character >>

with open("402-awesome_people5.txt", "r+") as file:

    print(file.read(7))                             # line nu

file.close()                                        # close the file, to save resources etc