'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

ALGO
---
1. 2 same length words are anagrams if they have the same letter frequencies - i.e. abc, cba, acb etc. all have 1 a, 1 b, 1 c
2. For each index, get the frequencies of the sub string and compare it to the frequencies of p

Optimization: Instead of creating a new counter, we can just update the one we have.
              When we move to a new index, eg. abcdef - first we had abc, then bcd, then cde - we remove the first letter from frequencies, and add the last
              to get the frequencies of the sub string
'''
from typing import List
from collections import Counter


class Solution:
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        def is_match(p_counts, s_counts):
            for ch in p_counts:
                if ch not in s_counts or s_counts[ch] != p_counts[ch]:
                    return False
            return True

        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []

        # frequencies of letters in p and first part of s
        p_counts = Counter(p)

        indices = []

        for i in range(0, s_len - p_len + 1):
            s_counts = Counter(s[i: i + p_len])
            if is_match(p_counts, s_counts):
                indices.append(i)

        return indices

    # optimized
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def is_match(p_counts, s_counts):
            for ch in p_counts:
                if ch not in s_counts or s_counts[ch] != p_counts[ch]:
                    return False
            return True

        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []

        # frequencies of letters in p and first part of s
        p_counts = Counter(p)
        s_counts = Counter(s[:p_len])

        indices = []
        if is_match(p_counts, s_counts):
            indices.append(0)

        for i in range(1, s_len - p_len + 1):
            s_counts[s[i - 1]] -= 1
            s_counts[s[i + p_len - 1]] += 1
            if is_match(p_counts, s_counts):
                indices.append(i)

        return indices


solution = Solution()
assert solution.findAnagrams('cbaebabacd', 'abc') == [0, 6]
assert solution.findAnagrams('abab', 'ab') == [0, 1, 2]
assert solution.findAnagrams('abc', 'cd') == []
