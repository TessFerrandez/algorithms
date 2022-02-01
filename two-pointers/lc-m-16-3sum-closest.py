'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_sum = sum(nums[:3])
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = sum((nums[i], nums[left], nums[right]))
                if abs(current_sum - target) < abs(best_sum - target):
                    best_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return best_sum
        return best_sum


solution = Solution()
assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
assert solution.threeSumClosest([0, 0, 0], 1) == 0
