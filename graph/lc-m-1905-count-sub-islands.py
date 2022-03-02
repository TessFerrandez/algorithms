'''
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
'''
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(row, col, visited):
            if 0 <= row < rows and 0 <= col < cols and grid2[row][col] == 1:
                grid2[row][col] = 2
                visited.add((row, col))
                dfs(row + 1, col, visited)
                dfs(row - 1, col, visited)
                dfs(row, col + 1, visited)
                dfs(row, col - 1, visited)

        def is_subisland(visited):
            for r, c in visited:
                if grid1[r][c] != 1:
                    return False
            return True

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    visited = set()
                    dfs(row, col, visited)
                    if is_subisland(visited):
                        count += 1

        return count


solution = Solution()
assert solution.countSubIslands([[1,1,1,0,0],
                                 [0,1,1,1,1],
                                 [0,0,0,0,0],
                                 [1,0,0,0,0],
                                 [1,1,0,1,1]],
                                [[1,1,1,0,0],
                                 [0,0,1,1,1],
                                 [0,1,0,0,0],
                                 [1,0,1,1,0],
                                 [0,1,0,1,0]]) == 3
assert solution.countSubIslands(grid1=[[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2=[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]) == 2
