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

import threading


class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.word_counts = {}

    def process_text(self, text):
        words = text.split(" ")
        for word in words:
            self._increment_word_count(word)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.word_counts.get(word, 0)
        self.lock.release()
        return count

    def _increment_word_count(self, word):
        self.lock.acquire()
        self.word_counts[word] = self.word_counts.get(word, 0) + 1
        self.lock.release()


###################################
# 400.04 - Thread Safe Counter - SOLUTION
###################################        

import threading


class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.word_counts = {}

    def process_text(self, text):
        words = text.split(" ")
        temporary_word_counts = {}
        for word in words:
            if word not in temporary_word_counts:
                temporary_word_counts[word] = 0
            temporary_word_counts[word] += 1
        self._increase_word_counts(temporary_word_counts)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.word_counts.get(word, 0)
        self.lock.release()
        return count

    def _increase_word_counts(self, word_counts):
        self.lock.acquire()
        for word in word_counts:
            self.word_counts[word] = self.word_counts.get(word, 0) + word_counts[word]
        self.lock.release()
