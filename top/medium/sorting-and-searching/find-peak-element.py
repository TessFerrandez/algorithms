from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        prev = -float('inf')

        for i in range(len(nums) - 1):
            if nums[i] > prev and nums[i] > nums[i + 1]:
                return i
            prev = nums[i]

        return len(nums) - 1


solution = Solution()
assert solution.findPeakElement([1, 2, 3, 1]) == 2
assert solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 1
