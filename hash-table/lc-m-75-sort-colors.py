'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''
from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        idx = 0
        for i in range(3):
            for _ in range(counts[i]):
                nums[idx] = i
                idx += 1


solution = Solution()

array = [2, 0, 2, 1, 1, 0]
solution.sortColors(array)
assert array == [0, 0, 1, 1, 2, 2]

array = [2, 0, 1]
solution.sortColors(array)
assert array == [0, 1, 2]
