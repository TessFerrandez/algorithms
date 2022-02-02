'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1
        current = 0

        while current <= end:
            if nums[current] == val:
                while end > current and nums[end] == val:
                    end -= 1
                nums[current] = nums[end]
                end -= 1
            current += 1

        return max(0, end + 1)


solution = Solution()

nums = [4, 5]
n = solution.removeElement(nums, 5)
assert nums[:n] == [4]

nums = [3, 3, 2, 2]
n = solution.removeElement(nums, 3)
assert nums[:n] == [2, 2]

nums = [3, 3]
n = solution.removeElement(nums, 3)
assert nums[:n] == []

nums = [1]
n = solution.removeElement(nums, 1)
assert nums[:n] == []

nums = [3, 2, 2, 3]
n = solution.removeElement(nums, 3)
assert nums[:n] == [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
n = solution.removeElement(nums, 2)
assert nums[:n] == [0, 1, 4, 0, 3]
