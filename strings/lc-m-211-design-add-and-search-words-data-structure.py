'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''
from collections import defaultdict
import re


class WordDictionary:
    def __init__(self):
        self.dictionary = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dictionary[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' in word:
            pattern = '^' + word + '$'
            for w in self.dictionary[len(word)]:
                if re.match(pattern, w):
                    return True
            return False
        else:
            return word in self.dictionary[len(word)]


words = WordDictionary()
words.addWord('bad')
words.addWord('dad')
words.addWord('mad')
assert not words.search('pad')
assert words.search('bad')
assert words.search('.ad')
assert words.search('b..')
assert not words.search('c..')
assert not words.search('c...')
