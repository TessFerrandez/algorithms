'''
'''
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        prev = -float('inf')

        for i, num in enumerate(nums):
            if num < prev:
                return i - 1
            prev = num

        return len(nums) - 1


solution = Solution()
assert solution.findPeakElement([-2147483648]) == 0
assert solution.findPeakElement([1, 2, 3, 1]) == 2
assert solution.findPeakElement([1, 2, 1, 2, 3, 5, 6, 4]) == 1
