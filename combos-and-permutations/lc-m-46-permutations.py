'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        permutations = []
        for i in range(len(nums)):
            num = nums[i]
            rest = nums[:i] + nums[i + 1:]
            for permutation in self.permute(rest):
                permutations.append([num] + permutation)

        return permutations

    def permute1(self, nums: List[int]) -> List[List[int]]:
        return [list(permutation) for permutation in permutations(nums)]


solution = Solution()
assert solution.permute([1, 2, 3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
assert solution.permute([0, 1]) == [[0, 1], [1, 0]]
assert solution.permute([1]) == [[1]]
