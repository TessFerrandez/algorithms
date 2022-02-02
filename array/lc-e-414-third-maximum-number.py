'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
'''
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        if len(unique) < 3:
            return unique[-1]
        else:
            return unique[-3]


solution = Solution()
assert solution.thirdMax([3, 2, 1]) == 1
assert solution.thirdMax([1, 2]) == 2
assert solution.thirdMax([2, 2, 3, 1]) == 1
