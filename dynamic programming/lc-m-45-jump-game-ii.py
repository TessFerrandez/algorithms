'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

ALGORITHM
------------------
Ex. [2, 3, 1, 1, 4]

dp[0] = 1 + min(dp[1], dp[2])
dp[1] = 1 + min(dp[2], dp[3], dp[4])
dp[2] = 1 + min(dp[3])
dp[3] = 1 + min(dp[4])
dp[4] = 0   # 0 steps since this is our target

Start filling it out with the base case (4) - and never jump beyond 4
'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]

        for i in range(n - 2, -1, -1):
            nexts = [dp[nx] for nx in range(i + 1, min(i + nums[i] + 1, n))]
            if nexts:
                dp[i] = 1 + min(nexts)
            else:
                dp[i] = 10 ** 9     # 0 steps

        return dp[0]


solution = Solution()
assert solution.jump([1, 2]) == 1
assert solution.jump([2, 3, 1, 1, 4]) == 2
assert solution.jump([2, 3, 0, 1, 4]) == 2
