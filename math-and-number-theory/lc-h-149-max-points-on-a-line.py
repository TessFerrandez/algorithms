'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
'''
from typing import List
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        slopes = defaultdict(set)

        for i, point in enumerate(points):
            x, y = point
            for x2, y2 in points[i + 1:]:
                if (x - x2) == 0:
                    slope = float('inf')
                    m = x
                else:
                    slope = (y - y2) / (x - x2)
                    m = y - (slope * x)
                slopes[(slope, m)].add((x, y))
                slopes[(slope, m)].add((x2, y2))

        return max(len(slopes[s]) for s in slopes)


solution = Solution()
assert solution.maxPoints([[0, 0]]) == 1
assert solution.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
assert solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
