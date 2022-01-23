'''
Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.
'''
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums = sorted(nums)
        low, high = 1, len(nums) - 2

        while low <= len(nums) - 2 and nums[low] == nums[low -1]:
            low += 1
        while high >= 1 and nums[high] == nums[high + 1]:
            high -= 1

        return max(0, high - low + 1)


solution = Solution()
assert solution.countElements([-100000,-99999,-99999]) == 0
assert solution.countElements([11, 7, 2, 15]) == 2
assert solution.countElements([-3, 3, 3, 90]) == 2
