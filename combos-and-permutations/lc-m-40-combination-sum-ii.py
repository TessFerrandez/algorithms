'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
from typing import List
from itertools import combinations


class Solution:
    # too long execution
    def combinationSum2_1(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [candidate for candidate in candidates if candidate <= target]

        if not candidates:
            return []

        min_val = min(candidates)

        combos = []

        for i in range(1, (target // min_val) + 1):
            for combo in combinations(candidates, i):
                if sum(combo) == target:
                    sort_combo = sorted(combo)
                    if sort_combo not in combos:
                        combos.append(sort_combo)

        return combos

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        combos = []
        unique = set(candidates)
        for num in unique:
            if num == target:
                combos.append([num])
            if num < target:
                remaining = candidates[::]
                remaining.remove(num)
                for combo in self.combinationSum2(remaining, target - num):
                    sort_combo = sorted([num] + combo)
                    if sort_combo not in combos:
                        combos.append(sort_combo)
        return combos


solution = Solution()
print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
assert solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
assert solution.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
print(solution.combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27))
print(solution.combinationSum2([2], 1))
