###################################
# 400.04 - Thread Safe Counter
###################################

"""
create a [WordCounter] class 
- able to count words in large texts
- so that a user can quickly calculate how many times a specific word occurs in a string

implement following methods: 
- [process_text(text)] 
-- take in a string, [text], and update the internal attributes of WordCounter in a thread-safe manner 
-- you may assume that [text.split(" ")] is good enough to return the list of words in the passed text

- [get_word_count(word)]
-- should take n a strin, [text] and check how many times that word has been seen in all the texts that this 
--- [WordCounter] has processed. 
-- if this word has not been seen, return 0
"""

