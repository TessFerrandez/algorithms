'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
----
We already have the solution for the straight case (no circle)
Now we can choose to

a) rob the first house - then we can't rob the last
b) don't rob the first house - then we can rob the last

so the solution is

max(rob(nums[:-1]), rob(nums[1:]))
'''
from typing import List


def rob_straight(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    # one based to allow for i-2 which now becomes i - 1
    prev1, prev2 = 0, 0

    for num in nums:
        prev1, prev2 = max(prev2 + num, prev1), prev1

    return prev1


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(rob_straight(nums[:-1]), rob_straight(nums[1:]))


solution = Solution()
assert solution.rob([2, 3, 2]) == 3
assert solution.rob([1, 2, 3, 1]) == 4
