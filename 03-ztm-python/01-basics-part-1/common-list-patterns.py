basket15 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

# how long is my list?
print(len(basket15)) # 10

# now lets try a sorted, reverse, reversed list... (interview question?)

basket15.sort()
basket15.reverse()
print(basket15) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(basket15[::-1]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# you will see this list slicing often when playing with lists (especially in interview questions)

##############
# build a list by auto

basket16 = list(range(1,100)) # new list with 100 values = 0-99
print(basket16)

#########
# joins

theSentence = ' ' # empty string

theSentence.join(['this', 'is', 'a', 'sentence', 'from', 'a', 'list'])
print(theSentence) # returned an empty string....

# so what we need to do is create a new list like so

the_new_sentence = theSentence.join(['this', 'is', 'a', 'sentence', 'from', 'a', 'list'])
print(the_new_sentence) # this is a sentence from a list

### ALTERNATIVE JOIN 

the_3rd_sentence = ' '.join(['this', 'is', 'another', 'sentence', 'from', 'a', 'list'])
print(the_3rd_sentence) # this is another sentence from a list





