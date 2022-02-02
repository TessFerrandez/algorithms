'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
'''
from typing import List
from collections import Counter


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []

        for num in range(1, len(nums) + 1):
            if num not in counts:
                result.append(num)

        return result


solution = Solution()
assert solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
assert solution.findDisappearedNumbers([1, 1]) == [2]
