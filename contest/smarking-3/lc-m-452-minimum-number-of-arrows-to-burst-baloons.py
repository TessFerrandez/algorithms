from cmath import inf
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        arrows = 1
        current_end = inf

        for start, end in points:
            if start > current_end:
                arrows += 1
                current_end = end
            else:
                current_end = min(current_end, end)

        return arrows


solution = Solution()
assert solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
assert solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
assert solution.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2
