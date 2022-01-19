'''
Given the pixels of an image, and a pixel[row and a column].
Recolor any neighbors of the pixel (left, right, up, down)
And any neighbors of the neighbors etc. with the newColor if the neighbors
have the same color as the current pixel

Ex.
111
110
101

[1, 1] => 2

Gives

222
220
201
'''
from typing import List
from collections import deque


def get_neighbors(pixel, image):
    r, c = pixel
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if r < len(image) - 1:
        neighbors.append((r + 1, c))
    if c < len(image[0]) - 1:
        neighbors.append((r, c + 1))
    return neighbors


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        todo = deque([(sr, sc)])
        visited = set()

        while todo:
            r, c = todo.popleft()
            image[r][c] = newColor
            visited.add((r, c))

            for nr, nc in get_neighbors((r, c), image):
                if (nr, nc) not in visited and image[nr][nc] == color:
                    todo.append((nr, nc))

        return image


solution = Solution()
assert solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0 ,1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
assert solution.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2) == [[2, 2, 2], [2, 2, 2]]
assert solution.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1) == [[0, 0, 0], [0, 1, 1]]