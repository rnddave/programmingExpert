# what is a truthy / falsey? 

# so far we saw booleans as values...
# but python can do other things as well 
# consider the following

isTrue = True
isFalse = False

if isTrue and isFalse:
    print('A > yes they are both True')
else:
    print('A > they are not both True')
# A > they are not both True

#----------------------------
# but if we change this as follows: 

isTrueb = 'hello'
isFalseb = 5

if isTrueb and isFalseb:
    print('B > yes they are both True')
else:
    print('B > they are not both True')
# B > yes they are both True

# this is because python is doing type-conversion 
# example isTrueb = bool('hello')
# this is a truthy value in python
# so what does this mean? 
# this means that the a string that is not empty or an integer that is not 0 will always be True
#----------------------------

isTrueC = 'hello'
isFalseC = 0
isTrueD = ''
isFalseD = 1

if isTrueC and isFalseC:
    print('C > yes they are both True')
else:
    print('C > they are not both True')
# C > they are not both True

if isTrueD and isFalseD:
    print('D > yes they are both True')
else:
    print('D > they are not both True')
#D > they are not both True

if isTrueD and isFalseC:
    print('DC > they are both True')
else:
    print('DC > they are both False')
#DC > they are both False

# more info here: 
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

