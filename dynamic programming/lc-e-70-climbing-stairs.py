'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]     # 1 ways to get up to 0 and 1 ways to get to 1

        for step in range (2, n + 1):
            dp.append(dp[step - 2] + dp[step - 1])

        return dp[n]


solution = Solution()
assert solution.climbStairs(2) == 2
assert solution.climbStairs(3) == 3
assert solution.climbStairs(4) == 5
