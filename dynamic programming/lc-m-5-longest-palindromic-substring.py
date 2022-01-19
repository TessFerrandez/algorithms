'''
Given a string 'aababad' find the longest palindromic substring ('ababa')

Algorightm.

1. All single character strings are palindromic [a, a, b, a, b, a, d]
2. All double character strings are palindromic if s[start] == s[end] [aa]
3. All longer strings are palindromic if s[start] == s[end] and the string between start and end is palindromic
[aba, bab, ababa]

Create a table (dp) where cols are "start" and rows are "end" (that will be filled with True if it is palindromic)
initially set to False

    1. set all single chars to True

  a     a     b     a     b     a     d
a True  False False False False False False
a False True  False False False False False
b False False True  False False False False
a False False False True  False False False
b False False False False True  False False
a False False False False False True  False
d False False False False False False True

    2. for all [start]/[end] - set to true if str between is empty (double char)
       or palindromic
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        dp = [[False for _ in range(str_len)] for __ in range(str_len)]
        max_len, start_i, end_i = 0, 0, 0

        for start in range(str_len, -1, -1):
            for end in range(start, str_len):
                if start == end:
                    # single character
                    dp[start][end] = True
                elif s[start] == s[end]:
                    if end - start == 1:
                        # a double character
                        dp[start][end] = True
                    else:
                        # outer chars ar the same
                        # this is a palindrome if the letters
                        # between is a palindrome
                        dp[start][end] = dp[start + 1][end - 1]
                if dp[start][end] and end - start >= max_len:
                    max_len = end - start
                    start_i = start
                    end_i = end

        return s[start_i: end_i + 1]


solution = Solution()
assert solution.longestPalindrome('babad') == 'bab'
assert solution.longestPalindrome('cbbd') == 'bb'
