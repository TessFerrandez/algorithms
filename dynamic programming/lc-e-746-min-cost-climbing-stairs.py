'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
from asyncio.proactor_events import constants
from typing import List


class Solution:
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        stairs = len(cost)
        if stairs <= 1:
            return 0

        dp = cost[:2]
        for c in cost[2:]:
            dp.append(c + min(dp[-2], dp[-1]))

        return min(dp[-2], dp[-1])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs = len(cost)
        if stairs <= 1:
            return 0

        prev0, prev1 = cost[0], cost[1]
        for c in cost[2:]:
            current = c + min(prev0, prev1)
            prev0, prev1 = prev1, current

        return min(prev0, prev1)


solution = Solution()
assert solution.minCostClimbingStairs([10, 15, 20]) == 15
assert solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
