'''
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
'''
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum(nums[1::2])


solution = Solution()
assert solution.arrayPairSum([1, 4, 3, 2]) == 4
assert solution.arrayPairSum([6, 2, 6, 5, 1, 2]) == 9
