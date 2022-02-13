class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {-1: 0, 0: 1}

        for stair in range(1, n + 1):
            ways[stair] = ways[stair - 1] + ways[stair - 2]

        return ways[n]


solution = Solution()
assert solution.climbStairs(2) == 2
assert solution.climbStairs(3) == 3
