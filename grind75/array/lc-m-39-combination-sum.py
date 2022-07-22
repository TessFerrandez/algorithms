from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        n = len(candidates)

        def dfs(idx, target, path):
            if target < 0:
                return
            if target == 0:
                results.append(path)
                return
            for i in range(idx, n):
                dfs(i, target - candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return results


solution = Solution()
assert solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
assert solution.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
assert solution.combinationSum([2], 1) == []
