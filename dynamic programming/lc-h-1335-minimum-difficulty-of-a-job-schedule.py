from functools import cache
from math import inf
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        @cache
        def min_difficulty(index, d, current):
            if index == n and d == 0:
                return current
            if index >= n or d <= 0:
                return inf

            current_max = max(current, jobDifficulty[index])
            return min(min_difficulty(index + 1, d, current_max), current_max + min_difficulty(index + 1, d - 1, 0))

        answer = min_difficulty(0, d, 0)
        return answer if answer != inf else -1


solution = Solution()
assert solution.minDifficulty([6,5,4,3,2,1], 2) == 7
assert solution.minDifficulty([9,9,9], 4) == -1
assert solution.minDifficulty([1,1,1], 3) == 3
