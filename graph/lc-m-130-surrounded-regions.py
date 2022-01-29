'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def build_graph(grid):
            graph = {}
            for y, row in enumerate(board):
                for x, ch in enumerate(row):
                    if ch == 'O':
                        graph[(x, y)] = True

            return graph

        def get_neighbors(position):
            x, y = position
            return [(x + dx, y + dy) for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]]

        def explore_land(graph, current, visited, current_land):
            if current in visited:
                return False

            visited.add(current)
            current_land.add(current)

            for neighbor in get_neighbors(current):
                if neighbor in graph:
                    explore_land(graph, neighbor, visited, current_land)

            return True

        def is_edge(land, h, w):
            x, y = land
            for x, y in get_neighbors((x, y)):
                if x < 0 or y < 0 or x >= w or y >= h:
                    return True
            return False

        def capture(land_area, board):
            h, w = len(board), len(board[0])
            for land in land_area:
                if is_edge(land, h, w):
                    return

            for x, y in land_area:
                board[y][x] = 'X'

        graph = build_graph(board)
        visited = set()

        for land in graph:
            current_land = set()
            if explore_land(graph, land, visited, current_land):
                capture(current_land, board)


solution = Solution()
grid = [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]
solution.solve(grid)
assert grid == [["X","X","X","X"],
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","O","X","X"]]

grid = [["X"]]
solution.solve(grid)
assert grid == [["X"]]
