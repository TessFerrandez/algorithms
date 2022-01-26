'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
'''
from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
        for ch in t:
            counts[ch] -= 1
            if counts[ch] < 0:
                return ch
        return ""