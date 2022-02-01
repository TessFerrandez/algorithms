'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        permutations = []

        unique = set(nums)
        for num in unique:
            remaining = nums[::]
            remaining.remove(num)
            for perm in self.permuteUnique(remaining):
                permutations.append([num] + perm)

        return permutations


solution = Solution()
assert solution.permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
