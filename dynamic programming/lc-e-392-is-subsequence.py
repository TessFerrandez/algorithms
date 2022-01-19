'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)

        if s_len == 0:
            return True

        i = 0
        for ch in t:
            if s[i] == ch:
                i += 1
                if i == s_len:
                    return True

        return False

    def isSubsequence2(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)


solution = Solution()
assert solution.isSubsequence('axc', 'ahbgdc') == False
assert solution.isSubsequence('abc', 'ahbgdc') == True
