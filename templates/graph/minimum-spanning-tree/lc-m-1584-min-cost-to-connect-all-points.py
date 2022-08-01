from collections import defaultdict
from typing import List
from Prims import prim_minimum_spanning_tree_cost


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        adj_list = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append([j, dist])
                adj_list[j].append([i, dist])

        _, cost = prim_minimum_spanning_tree_cost(adj_list)
        return cost


solution = Solution()
assert solution.minCostConnectPoints([[0, 0]]) == 0
assert solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
assert solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
