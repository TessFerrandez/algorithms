'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
'''
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combo_rec(nums: List[int], k: int) -> List[List[int]]:
            if k == 0:
                return [[]]

            combos = []

            for j in range(0, len(nums)):
                for sub_combos in combo_rec(nums[j + 1:], k - 1):
                    combos.append([nums[j]] + sub_combos)

            return combos

        nums = [i for i in range(1, n + 1)]
        return combo_rec(nums, k)

    def combine1(self, n: int, k: int) -> List[List[int]]:
        return [list(combination) for combination in combinations(range(1, n + 1), k)]


solution = Solution()
assert solution.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
assert solution.combine(1, 1) == [[1]]
