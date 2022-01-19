def interleaves(s1, i, s2, j, s3, k, memo):
    if i == len(s1):
        return s2[j:] == s3[k:]

    if j == len(s2):
        return s1[i:] == s3[k:]

    memo[i][j] == 1

    answer = False
    if s3[k] == s1[i] and interleaves(s1, i + 1, s2, j, s3, k + 1, memo) or s3[k] == s2[j] and interleaves(s1, i, s2, j + 1, s3, k + 1, memo):
        answer = True
    memo[i][j] = 1 if answer else 0
    return answer


class Solution:
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
        return interleaves(s1, 0, s2, 0, s3, 0, memo)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

        return dp[len(s1)][len(s2)]


solution = Solution()
assert solution.isInterleave("", "", "") == True
assert solution.isInterleave("a", "", "a") == True
assert solution.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
assert solution.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
