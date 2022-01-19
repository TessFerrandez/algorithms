'''
Solution using dynamic programming
-----------------------------------
Given a matrix, return the distance to the nearest 0
for each cell

Ex:
0 0 0
0 1 0
1 1 1
=>
0 0 0
0 1 0
1 2 1
'''
from typing import List
from collections import deque


def get_neighbors(cx, cy, width, height):
    neighbors = []
    if cx > 0:
        neighbors.append((cx - 1, cy))
    if cy > 0:
        neighbors.append((cx, cy - 1))
    if cx < width - 1:
        neighbors.append((cx + 1, cy))
    if cy < height - 1:
        neighbors.append((cx, cy + 1))
    return neighbors


def find_distance(x, y, mat, width, height) -> int:
    if mat[y][x] == 0:
        return 0

    todo = deque([(x, y, 0)])
    visited = set()

    while todo:
        cx, cy, dist = todo.popleft()
        if (cx, cy) not in visited:
            visited.add((cx, cy))

            if mat[cy][cx] == 0:
                return dist

            for nx, ny in get_neighbors(cx, cy, width, height):
                todo.append((nx, ny, dist + 1))


class Solution:
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        width, height = len(mat[0]), len(mat)
        result = [[0 for _ in range(width)] for _ in range(height)]
        for y in range(height):
            for x in range(width):
                result[y][x] = find_distance(x, y, mat, width, height)

        return result

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        width, height = len(mat[0]), len(mat)
        result = [[-1 for _ in range(width)] for _ in range(height)]

        changed = []
        for y in range(height):
            for x in range(width):
                if mat[y][x] == 0:
                    result[y][x] = 0
                    changed.append((x, y))

        while changed:
            new_changed = []
            for x, y in changed:
                dist = result[y][x]
                for (nx, ny) in get_neighbors(x, y, width, height):
                    if result[ny][nx] == -1:
                        result[ny][nx] = dist + 1
                        new_changed.append((nx, ny))
            changed = new_changed

        return result


solution = Solution()
print(solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
