from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    # my solution - using memoization
    def canCross1(self, stones: List[int]) -> bool:
        stonies = set(stones)

        @cache
        def can_cross(stone, jumps, target):
            if stone == target:
                return True
            if stone > target:
                return False
            for j in [jumps - 1, jumps, jumps + 1]:
                if j > 0 and (stone + j) in stonies:
                    if can_cross(stone + j, j, target):
                        return True
            return False

        if (stones[0] + 1) not in stonies:
            return False
        return can_cross(stones[0] + 1, 1, stones[-1])

    # dp solution
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = defaultdict(lambda: False)
        dp[(0, 1)] = True

        for i in range(1, n):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff < 0 or diff > n or not dp[(j, diff)]:
                    continue
                dp[(i, diff)] = True
                if diff - 1 >= 0:
                    dp[(i, diff - 1)] = True
                if diff + 1 <= n:
                    dp[(i, diff + 1)] = True
                if i == n - 1:
                    return True


solution = Solution()
assert not solution.canCross([0, 2])
assert solution.canCross([0,1,3,5,6,8,12,17])
assert not solution.canCross([0,1,2,3,4,8,9,11])
