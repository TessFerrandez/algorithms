'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        combos = []
        for i in range(2 ** len(nums)):
            combo = []
            j = 0
            while i > 0:
                if i % 2:
                    combo.append(nums[j])
                i = i >> 1
                j += 1

            combo = sorted(combo)
            if combo not in combos:
                combos.append(combo)
        return combos


solution = Solution()
assert solution.subsetsWithDup([1, 2, 2]) == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
assert solution.subsetsWithDup([4, 4, 4, 1, 4]) == [[], [4], [4, 4], [4, 4, 4], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [4, 4, 4, 4], [1, 4, 4, 4, 4]]
