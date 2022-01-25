'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num < 0:
            return max_num

        max_sum = - 2 ** 31
        current_sum = 0
        for num in nums:
            current_sum = max(0, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


solution = Solution()
assert solution.maxSubArray([-2,-3,-1]) == -1
assert solution.maxSubArray([-2,-1]) == -1
assert solution.maxSubArray([-2,1]) == 1
assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert solution.maxSubArray([-1]) == -1
assert solution.maxSubArray([1]) == 1
assert solution.maxSubArray([5,4,-1,7,8]) == 23
