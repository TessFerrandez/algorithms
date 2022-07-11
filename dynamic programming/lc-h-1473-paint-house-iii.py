from functools import cache
from math import inf
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        num_houses = m
        total_colors = n

        @cache
        def find_min(current_idx, neighborhoods, prev_color):
            if current_idx == num_houses:
                return 0 if neighborhoods == target else inf

            if neighborhoods > target:
                return inf

            min_cost = inf
            if houses[current_idx] != 0:
                new_neighborhoods = neighborhoods + (1 if houses[current_idx] != prev_color else 0)
                min_cost = find_min(current_idx + 1, new_neighborhoods, houses[current_idx])
            else:
                for color in range(1, total_colors + 1):
                    new_neighborhoods = neighborhoods + (1 if color != prev_color else 0)
                    current_cost = cost[current_idx][color - 1] + find_min(current_idx + 1, new_neighborhoods, color)
                    min_cost = min(min_cost, current_cost)

            return min_cost

        answer = find_min(0, 0, 0)
        return -1 if answer == inf else answer


solution = Solution()
assert solution.minCost([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3) == 9
assert solution.minCost([0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3) == 11
assert solution.minCost([3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3) == -1
