lst = [1, 2, 3]
print(lst[0])
print(lst[1])
print(lst[2])

lst = ["Hello", "World"]
lst.append("!")
print(lst[0], lst[1], lst[2])

print(len(lst))

# test yourself

string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
string3 = input("Enter a string: ")
string4 = input("Enter a string: ")
string5 = input("Enter a string: ")

strings = [string1, string2, string3, string4, string5]

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

final_string = strings[num1] + strings[num2] + strings[num3]
print(final_string)

# another option for test number 1

string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
string3 = input("Enter a string: ")
string4 = input("Enter a string: ")
string5 = input("Enter a string: ")

strings = []
strings.append(string1)
strings.append(string2)
strings.append(string3)
strings.append(string4)
strings.append(string5)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

final_string = strings[num1] + strings[num2] + strings[num3]
print(final_string)

# another option for test number 1

strings = [
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
]

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

final_string = strings[num1] + strings[num2] + strings[num3]
print(final_string)

