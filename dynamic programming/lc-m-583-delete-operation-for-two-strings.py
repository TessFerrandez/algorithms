'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def longestCommonSubsequence(text1: str, text2: str) -> int:
            dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
            for i in range(len(text1)):
                for j in range(len(text2)):
                    if text1[i] == text2[j]:
                        dp[i + 1][j + 1] = dp[i][j] + 1
                    else:
                        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

            return dp[len(text1)][len(text2)]

        subsequence_length = longestCommonSubsequence(word1, word2)
        return len(word1) + len(word2) - 2 * subsequence_length


solution = Solution()
assert solution.minDistance('sea', 'eat') == 2
assert solution.minDistance('leetcode', 'etco') == 4
