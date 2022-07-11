from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        result = [[-1 for _ in range(cols)] for _ in range(rows)]

        todo = deque([(r, c, 0) for r in range(rows) for c in range(cols) if mat[r][c] == 0])
        while todo:
            row, col, steps = todo.popleft()
            if result[row][col] == -1:
                result[row][col] = steps

            for nr, nc in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                if 0 <= nr < rows and 0 <= nc < cols and result[nr][nc] == -1:
                    todo.append((nr, nc, steps + 1))

        return result


solution = Solution()
assert solution.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
assert solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
