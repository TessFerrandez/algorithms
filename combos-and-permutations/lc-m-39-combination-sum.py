'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        combos = []

        for num in candidates:
            if num == target:
                combos.append([num])
            if num < target:
                for combo in self.combinationSum(candidates, target - num):
                    combo_sort = sorted([num] + combo)
                    if combo_sort not in combos:
                        combos.append(combo_sort)

        return combos


solution = Solution()
assert solution.combinationSum([1, 2], 3) == [[1, 1, 1], [1, 2]]
assert solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
assert solution.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
