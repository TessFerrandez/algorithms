from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(stairs):
            if stairs == 0:
                return 1
            if stairs < 0:
                return 0
            return climb(stairs - 1) + climb(stairs - 2)

        return climb(n)


solution = Solution()
assert solution.climbStairs(2) == 2
assert solution.climbStairs(3) == 3
