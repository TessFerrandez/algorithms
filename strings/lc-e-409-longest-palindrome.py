'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        length = 0
        for ch in counts:
            if counts[ch] > 1:
                length += (counts[ch] // 2) * 2

        for ch in counts:
            if counts[ch] % 2:
                length += 1
                break

        return length


solution = Solution()
assert solution.longestPalindrome('abccccdd') == 7
assert solution.longestPalindrome('a') == 1
assert solution.longestPalindrome('bb') == 2
