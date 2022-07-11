from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image

        rows, cols = len(image), len(image[0])
        todo = deque([(sr, sc)])

        while todo:
            r, c = todo.popleft()
            image[r][c] = newColor

            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old_color:
                    todo.append((nr, nc))

        return image


solution = Solution()
assert solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
assert solution.floodFill([[0,0,0],[0,0,0]], 0, 0, 0) == [[0,0,0],[0,0,0]]
