from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        lines = defaultdict(set)

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:
                    k = float('inf')
                    m = x1
                else:
                    k = (y1 - y2) / (x1 - x2)
                    m = y1 - (x1 * k)
                lines[(k, m)].add((x1, y1))
                lines[(k, m)].add((x2, y2))

        return max(len(lines[c]) for c in lines)


solution = Solution()
assert solution.maxPoints([[0,0]]) == 1
assert solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
assert solution.maxPoints([[1,1],[2,2],[3,3]]) == 3
