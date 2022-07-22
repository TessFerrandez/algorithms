'''
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
'''
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for word in words if word.startswith(pref))


solution = Solution()
assert solution.prefixCount(["pay", "attention", "practice", "attend"], 'at') == 2
assert solution.prefixCount(["leetcode", "win", "loops", "success"], 'code') == 0
