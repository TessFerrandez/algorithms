from math import sqrt
from typing import List


class Solution:
    # TLE
    def countLatticePoints1(self, circles: List[List[int]]) -> int:
        def get_points(x, y, r):
            points = set()

            for row in range(y - r, y + r + 1):
                for col in range(x - r, x + r + 1):
                    if sqrt((col - x) ** 2 + (row - y) ** 2) <= r:
                        points.add((col, row))

            return points

        points = set()

        for x, y, r in circles:
            new_points = get_points(x, y, r)
            points.update(new_points)

        return len(points)

    # counting only a quarter of the points
    def countLatticePoints2(self, circles: List[List[int]]) -> int:
        points = set()

        for x, y, r in circles:
            for cx in range(x + 1, x + r + 1):
                for cy in range(y + 1, y + r + 1):
                    if sqrt((cx - x) ** 2 + (cy - y) ** 2) <= r:
                        points.add((cx, cy))
                        points.add((2 * x - cx, cy))
                        points.add((2 * x - cx, 2 * y - cy))
                        points.add((cx, 2 * y - cy))
            for cy in range(y - r, y + r + 1):
                points.add((x, cy))
            for cx in range(x - r, x + r + 1):
                points.add((cx, y))

        return len(points)

    # optimized
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()

        for x, y, r in circles:
            for dx in range(r + 1):
                y_upper = int((r ** 2 - dx ** 2) ** 0.5)
                for dy in range(y_upper + 1):
                    points.add((x + dx, y + dy))
                    points.add((x + dx, y - dy))
                    points.add((x - dx, y + dy))
                    points.add((x - dx, y - dy))

        return len(points)


solution = Solution()
assert solution.countLatticePoints([[2, 2, 1]]) == 5
assert solution.countLatticePoints([[2, 2, 2], [3, 4, 1]]) == 16
