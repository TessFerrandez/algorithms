from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs = 0

        for x1, y1 in points:
            distances = defaultdict(int)
            for x2, y2 in points:
                distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
                distances[distance] += 1
            for distance in distances:
                boomerangs += distances[distance] * (distances[distance] - 1)
        return boomerangs


solution = Solution()
assert solution.numberOfBoomerangs([[0,0],[1,0],[2,0]]) == 2
assert solution.numberOfBoomerangs([[1,1],[2,2],[3,3]]) == 2
assert solution.numberOfBoomerangs([[1,1]]) == 0
