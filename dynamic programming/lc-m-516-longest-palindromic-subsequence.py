'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

ALGO:
The problem can be reduced to finding the longest common subsequence between the string and its reverse string
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def longest_common_subsequence(text1, text2):
            dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
            for i in range(len(text1)):
                for j in range(len(text2)):
                    if text1[i] == text2[j]:
                        dp[i + 1][j + 1] = dp[i][j] + 1
                    else:
                        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

            return dp[len(text1)][len(text2)]

        return longest_common_subsequence(s, s[::-1])


solution = Solution()
assert solution.longestPalindromeSubseq('bbbab') == 4
assert solution.longestPalindromeSubseq('cbbd') == 2
