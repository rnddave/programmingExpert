# only people over 18 can drive the car: 

age = 0
license = False

def canYouDrive(age, license):
    if (age > 17 and license == True):
        print('you can drive')
    elif (age > 17 and license == False):
        print('you need a licese first')
    else:
        print(' you are too young to drive ')

age = int(input('how old are you? ' ))
license = input('do you have a license? ' )

if (license == 'yes' or license == 'y'):
    license = True
else:
    license = False

canYouDrive(age, license)
 
# just a silly conditional check ^^












