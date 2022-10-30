from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        max_row, max_col = rows - 1, cols - 1

        if rows == 1 and cols == 1:
            return 0

        todo = deque([(0, 0, k, 0)])      # row, col, allowed removes, steps
        visited = set([(0, 0, k)])      # row, col, allowed removes

        if k > (max_row + max_col):
            return max_row + max_col

        while todo:
            row, col, eliminate, steps = todo.popleft()
            for new_row, new_col in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == 1 and eliminate > 0 and (new_row, new_col, eliminate - 1) not in visited:
                        visited.add((new_row, new_col, eliminate - 1))
                        todo.append((new_row, new_col, eliminate - 1, steps + 1))
                    if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                        if new_row == max_row and new_col == max_col:
                            return steps + 1
                        visited.add((new_row, new_col, eliminate))
                        todo.append((new_row, new_col, eliminate, steps + 1))

        return -1


solution = Solution()
assert solution.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1) == 6
assert solution.shortestPath([[0,1,1],[1,1,1],[1,0,0]], 1) == -1
