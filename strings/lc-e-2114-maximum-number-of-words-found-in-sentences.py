'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
'''
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0

        for sentence in sentences:
            max_words = max(max_words, sentence.count(' ') + 1)

        return max_words


solution = Solution()
assert solution.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]) == 6
assert solution.mostWordsFound(["much"]) == 1
assert solution.mostWordsFound([]) == 0
assert solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]) == 3
