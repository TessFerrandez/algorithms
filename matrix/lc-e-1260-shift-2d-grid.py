from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift(grid):
            new_grid = []
            for row in grid:
                new_grid.append([row[-1]] + row[:-1])

            temp = new_grid[-1][0]
            for row in range(len(grid) - 2, -1, -1):
                new_grid[row + 1][0] = new_grid[row][0]
            new_grid[0][0] = temp

            return new_grid

        for _ in range(k):
            grid = shift(grid)

        return grid


solution = Solution()
assert solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1) == [[9,1,2],[3,4,5],[6,7,8]]
assert solution.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4) == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
assert solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], k=9) == [[1,2,3],[4,5,6],[7,8,9]]
