'''
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
'''
from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])

        r, c = entrance
        visited = set([(r, c)])
        todo = deque([(0, r, c)])

        while todo:
            steps, r, c = todo.popleft()

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or maze[nr][nc] == '+' or (nr, nc) in visited:
                    continue

                if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                    return steps + 1

                visited.add((nr, nc))
                todo.append((steps + 1, nr, nc))

        return -1


solution = Solution()
assert solution.nearestExit([["+",".","+","+","+","+","+"],
                             ["+",".","+",".",".",".","+"],
                             ["+",".","+",".","+",".","+"],
                             ["+",".",".",".","+",".","+"],
                             ["+","+","+","+","+",".","+"]], [0, 1]) == 12
assert solution.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1, 2]) == 1
assert solution.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1, 0]) == 2
assert solution.nearestExit([[".","+"]], [0, 0]) == -1
