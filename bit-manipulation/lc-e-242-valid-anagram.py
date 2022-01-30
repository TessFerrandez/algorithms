'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)

        for ch in count_s:
            if ch not in count_t or count_s[ch] != count_t[ch]:
                return False
        return True


solution = Solution()
assert solution.isAnagram('anagram', 'nagaram')
assert not solution.isAnagram('rat', 'car')
