'''
Given an integer n, return the number of structurally
unique BST's (binary search trees) which has exactly n
nodes of unique values from 1 to n.
'''
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1]

        for i in range(2, n + 1):
            ways = 0

            k = i - 1
            for j in range(i // 2):
                ways += 2 * dp[j] * dp[k]
                k -= 1

            if i % 2:
                ways += dp[i // 2] * dp[k]

            dp.append(ways)

        return dp[n]


solution = Solution()
assert solution.numTrees(3) == 5
assert solution.numTrees(1) == 1
assert solution.numTrees(4) == 14
