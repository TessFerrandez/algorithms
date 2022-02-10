'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        dir = -1
        steps = n - 1

        matrix[0] = [i for i in range(1, n + 1)]
        num = n + 1
        x, y = n - 1, 0

        while steps > 0:
            for _ in range(2):
                dir = (dir + 1) % 4
                dx, dy = dirs[dir]
                for _ in range(steps):
                    x += dx
                    y += dy
                    matrix[y][x] = num
                    num += 1
            steps -= 1

        return matrix


solution = Solution()
assert solution.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert solution.generateMatrix(1) == [[1]]
