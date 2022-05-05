'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
from functools import cache
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

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        stairs = len(cost)
        if stairs <= 1:
            return 0

        prev0, prev1 = cost[0], cost[1]
        for c in cost[2:]:
            current = c + min(prev0, prev1)
            prev0, prev1 = prev1, current

        return min(prev0, prev1)

    # top down (template)
    def minCostClimbingStairs3(self, cost: List[int]) -> int:
        @cache
        def min_cost(step):
            if step <= 1:
                return 0
            return min(min_cost(step - 1) + cost[step - 1], min_cost(step - 2) + cost[step - 2])

        return min_cost(len(cost))

    # bottom up (template)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = {0: 0, 1: 0}

        for step in range(2, len(cost) + 1):
            min_cost[step] = min(min_cost[step - 1] + cost[step - 1], min_cost[step - 2] + cost[step - 2])

        return min_cost[len(cost)]


solution = Solution()
assert solution.minCostClimbingStairs([10, 15, 20]) == 15
assert solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
