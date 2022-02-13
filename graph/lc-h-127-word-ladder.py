'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        word_list = set(wordList)

        def is_one_off(word1, word2):
            num_off = 0
            for i in range(n):
                if word1[i] != word2[i]:
                    if num_off > 0:
                        return False
                    num_off += 1
            return num_off == 1

        def get_neighbor_words(word):
            neighbors = []

            for next_word in word_list:
                if is_one_off(word, next_word):
                    neighbors.append(next_word)

            return neighbors

        if endWord not in word_list:
            return 0

        if beginWord == endWord:
            return 1

        todo = deque([(beginWord, 1)])
        if beginWord in word_list:
            word_list.remove(beginWord)

        while todo:
            word, steps = todo.popleft()

            for next_word in get_neighbor_words(word):
                if next_word == endWord:
                    return steps + 1

                word_list.remove(next_word)
                todo.append((next_word, steps + 1))

        return 0


solution = Solution()
assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
