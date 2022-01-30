'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combos = []
        for i in range(2 ** len(nums)):
            combo = []
            j = 0
            while i > 0:
                if i % 2:
                    combo.append(nums[j])
                i = i >> 1
                j += 1
            combos.append(combo)
        return combos


solution = Solution()
assert solution.subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
