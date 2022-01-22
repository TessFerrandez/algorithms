'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid] == target:
                start = mid
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                end = mid
                while end + 1 < n and nums[end + 1] == target:
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]


solution = Solution()
assert solution.searchRange([1, 1, 2], 1) == [0, 1]
assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert solution.searchRange([], 0) == [-1, -1]
