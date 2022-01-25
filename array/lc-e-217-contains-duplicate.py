'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
from typing import List
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for num in nums:
            if num in counts:
                return True
            counts[num] += 1
        return False


solution = Solution()
assert solution.containsDuplicate([1, 2, 3, 1]) == True
assert solution.containsDuplicate([1, 2, 3, 4]) == False
assert solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
