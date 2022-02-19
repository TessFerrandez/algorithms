'''
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.
'''
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        last_val = -2

        for num in nums:
            if num > last_val + 1:
                last_val = num
            else:
                operations += last_val + 1 - num
                last_val += 1

        return operations


solution = Solution()
assert solution.minOperations([1, 1, 1]) == 3
assert solution.minOperations([1, 5, 2, 4, 1]) == 14
assert solution.minOperations([8]) == 0
