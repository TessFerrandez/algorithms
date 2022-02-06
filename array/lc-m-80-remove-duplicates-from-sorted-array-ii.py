'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        i = 2
        while i < n:
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                n -= 1
            else:
                i += 1
        return n


solution = Solution()

nums = [1, 1, 1, 2, 2, 3]
n = solution.removeDuplicates(nums)
assert nums[:n] == [1, 1, 2, 2, 3]

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
n = solution.removeDuplicates(nums)
assert nums[:n] == [0, 0, 1, 1, 2, 3, 3]
