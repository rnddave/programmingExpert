
# simple challenge - ask for year of birth and return 'you are x age old' 

from datetime import date

birth_year = int(input('what year were you born: '))

theYearToday = int(date.today().year)

# this bit is just me adding complexity to an otherwise simple challenge...
def generationY(birth_year):
    if (birth_year > 1945 and birth_year < 1965):
        return 'a Baby Boomer'
    elif (birth_year > 1964 and birth_year < 1981):
        return 'from Generation X (Gen X)'
    elif (birth_year > 1980 and birth_year < 1997):
        return 'a Millennial'
    elif (birth_year > 1996 and birth_year < 2013):
        return 'known as Gen Z'
    elif (birth_year > 2012 and birth_year < theYearToday):
        return 'known as Generation Alpha'
    else:
        return 'You are just really old!'

# print(type(theYearToday)) # testing
# print(theYearToday) # testing

yourAge = theYearToday - birth_year

print(f'Depending on the day you were born, you are either {yourAge -1} or {yourAge} years old and you are {generationY(birth_year)}')








