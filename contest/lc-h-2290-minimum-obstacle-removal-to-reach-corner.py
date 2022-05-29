from heapq import heappop, heappush
from math import inf
from queue import PriorityQueue
from typing import List


class Solution:
    # TLE - my solution
    def minimumObstacles1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def get_neighbors(row, col):
            neighbors = [(nr, nc) for nr, nc in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)] if 0 <= nr < rows and 0 <= nc < cols]
            return neighbors

        visited = set()
        costs = {(r, c): 10**9 for r in range(rows) for c in range(cols)}
        costs[(0, 0)] = 0

        todo = PriorityQueue()
        todo.put((0, (0, 0)))

        while not todo.empty():
            current_cost, (r, c) = todo.get()
            if (r, c) == (rows - 1, cols - 1):
                return current_cost

            visited.add((r, c))

            for nr, nc in get_neighbors(r, c):
                neighbor_cost = grid[nr][nc]
                if (nr, nc) not in visited:
                    old_cost = costs[(nr, nc)]
                    new_cost = current_cost + neighbor_cost
                    if new_cost < old_cost:
                        todo.put((new_cost, (nr, nc)))
                        costs[(nr, nc)] = new_cost

    # same but with heap instead of priority queue
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = map(len, (grid, grid[0]))
        obstacles = [[inf] * cols for _ in range(rows)]
        obstacles[0][0] = grid[0][0]

        heap = [(obstacles[0][0], 0, 0)]
        while heap:
            current_obstacles, r, c = heappop(heap)
            if (r, c) == (rows - 1, cols - 1):
                return current_obstacles

            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] + current_obstacles < obstacles[nr][nc]:
                    obstacles[nr][nc] = grid[nr][nc] + current_obstacles
                    heappush(heap, (obstacles[nr][nc], nr, nc))


solution = Solution()
assert solution.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]) == 2
assert solution.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]) == 0
