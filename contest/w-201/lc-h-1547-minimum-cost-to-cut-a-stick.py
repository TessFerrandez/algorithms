from functools import lru_cache
from typing import List


class Solution:
    # top down
    def minCost1(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def best_cuts(start, end):
            if end - start <= 1:
                return 0
            return min(cuts[end] - cuts[start] + best_cuts(start, cut) + best_cuts(cut, end) for cut in range(start + 1, end))

        cuts.extend([0, n])
        cuts.sort()
        return best_cuts(0, len(cuts) - 1)

    # bottom up
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()

        num_cuts = len(cuts)

        dp = [[0] * num_cuts for _ in range(num_cuts)]
        for i in range(2, num_cuts):
            for start in range(num_cuts - i):
                end = start + i
                dp[start][end] = min(cuts[end] - cuts[start] + dp[start][cut] + dp[cut][end] for cut in range(start + 1, end))

        return dp[0][-1]


solution = Solution()
assert solution.minCost(7, [1,3,4,5]) == 16
assert solution.minCost(9, [5, 6, 1, 4, 2]) == 22
