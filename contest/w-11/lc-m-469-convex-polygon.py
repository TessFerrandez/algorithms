from typing import List


class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        n = len(points)

        previous, current = 0, 0

        for i in range(n):
            x, y = points[i]
            x1, y1 = points[(i + 1) % n]
            x2, y2 = points[(i + 2) % n]

            current = (x1 - x) * (y2 - y1) - (x2 - x1) * (y1 - y)

            if current != 0:
                if (current > 0 and previous < 0) or (current < 0 and previous > 0):
                    return False
                else:
                    previous = current

        return True


solution = Solution()
assert solution.isConvex([[0,0],[0,1],[1,1],[1,0]])
assert not solution.isConvex([[0,0],[0,10],[10,10],[10,0],[5,5]])
