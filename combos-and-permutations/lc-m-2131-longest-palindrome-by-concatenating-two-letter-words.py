'''
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
'''
from typing import List
from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1
        word_map = dict(word_map)

        singles = 0
        pairs = 0
        for word in word_map:
            if word[0] == word[1]:
                pairs += (word_map[word] // 2) * 2
                singles += word_map[word] % 2
            else:
                pair_word = word[1] + word[0]
                if pair_word in word_map:
                    pairs += min(word_map[word], word_map[pair_word])

        pairs = pairs // 2
        singles = 1 if singles > 0 else 0
        return (2 * pairs + singles) * 2


solution = Solution()
assert solution.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]) == 22
assert solution.longestPalindrome(["lc","cl","gg"]) == 6
assert solution.longestPalindrome(["ab","ty","yt","lc","cl","ab"]) == 8
assert solution.longestPalindrome(["cc","ll","xx"]) == 2
