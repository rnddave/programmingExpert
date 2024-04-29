### 215.02 -- write a prog that asks for a number, keep asking until they enter 5, but then also print how many numbers they entered ###

number_of_entries = 0

while True:
    number = int(input("Enter a number: "))
    number_of_entries += 1

    if number == 5:
        break

print(f"You entered {number_of_entries} numbers.")



### 215.03 -- ask user to enter a word until they enter Q or QUIT, 
# then display the average length of all the words excluding the 'q' or 'quit' 
# If user doesn't enter anything beyond 'q' or 'quit' then the program should display no output ###

## >> Attempt 1 << ##

# # somewhere to hold the current value
# current_wrd = 0

# # probably need to know how many inputs the user made, in order to find the average
# num_of_words = len(wrd_lst)

# # You'll have to use the following strings:
# # 1) "Enter a word: "
# # 2) "The average word length is: _."

# while True:
#     wrd_lst_in = input("Enter a word: ")
#     wrd_lst.append(wrd_lst_in)
#     # average the number of characters in each list item
#     for item in wrd_lst:
#         current_wrd += len(item)
#     ave_len = int(wrd_lst) / int(num_of_words)

# print("The average word length is: {ave_len}.")

## >> Attempt 2 << ## 
# # decalre an empty list to store the words

# wrd_lst = []

# while True:
#     wrd_lst_in = input("Enter a word: ")
 
#     wrd_lst.append(wrd_lst_in)

#     if wrd_lst_in == "q" or "quit":
#         break

# avg_string_length = sum([len(i) for i in wrd_lst])/len(wrd_lst)
# print(f"The average word length is: {avg_string_length}.")

## Example from course ##

word_length_sum = 0
word_count = 0

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    word_length_sum += len(word)
    word_count += 1

if word_count > 0:
    average_word_length = word_length_sum / word_count
    print(f"The average word length is: {average_word_length}.")

## Alternative example ##

words = []

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    words.append(word)

if len(words) > 0:
    word_length_sum = 0

    for word in words:
        word_length_sum += len(word)

    average_word_length = word_length_sum / len(words)
    print(f"The average word length is: {average_word_length}.")


### 215.04 -- use a while loop to print the square of the numbers 1, 3, 6, 10, 15, 21 ###

nums = [1, 3, 6, 10, 15, 21]
i = 0

while i < len(nums):
    num = nums[i]
    print(num * num)

    i += 1