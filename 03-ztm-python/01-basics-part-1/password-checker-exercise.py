# we want to take a couple inputs (username and password)
# we want to give output that hides the password but comments on it length

username = input('what is your username? ')
password = input('what is your password? ')

hiddenPassword = len(password) * '*'

print(f'Hi {username}, I can see that your password is {hiddenPassword} which is {len(password)} characters long')

