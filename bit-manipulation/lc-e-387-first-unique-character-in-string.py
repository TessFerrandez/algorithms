'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
