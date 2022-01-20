'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
'''
from collections import Counter
from typing import List


def valid_word(ch_counts, word):
    word_count = Counter(word)
    for ch in word_count:
        if ch not in ch_counts or ch_counts[ch] < word_count[ch]:
            return False
    return True


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if not words:
            return True

        ch_counts = Counter(chars)
        return sum(len(word) for word in words if valid_word(ch_counts, word))


solution = Solution()
print(solution.countCharacters(["cat","bt","hat","tree"], 'atach'))
print(solution.countCharacters(["hello","world","leetcode"], 'welldonehoneyr'))
