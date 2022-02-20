'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
'''
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            if nums[i] < (nums[i + 1] + nums[i + 2]):
                return nums[i] + nums[i + 1] + nums[i + 2]

        return 0


solution = Solution()
assert solution.largestPerimeter([2, 1, 2]) == 5
assert solution.largestPerimeter([1, 2, 1]) == 0
assert solution.largestPerimeter([2, 1, 2, 7]) == 5
