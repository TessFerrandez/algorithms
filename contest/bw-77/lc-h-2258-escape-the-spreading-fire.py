from collections import deque
from copy import deepcopy
from typing import List


class Solution:
    # my contest solution - TLE
    def maximumMinutes1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def has_path(minutes):
            maze = deepcopy(grid)
            maze = spread_fire(maze, minutes)

            todo = deque([(0, 0, 0)])
            visited = set([(0, 0)])
            current_min = 0

            while todo:
                minute, r, c = todo.popleft()
                if (r, c) == (rows - 1, cols - 1):
                    return True

                if minute > current_min:
                    current_min += 1
                    fires = [[r, c] for r in range(rows) for c in range(cols) if maze[r][c] == 1]
                    for fr, fc in fires:
                        for nr, nc in (fr + 1, fc), (fr - 1, fc), (fr, fc + 1), (fr, fc - 1):
                            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                                maze[nr][nc] = 1

                if maze[r][c] == 1:
                    continue

                for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            todo.append((minute + 1, nr, nc))
            return False

        def spread_fire(maze, minutes):
            new_maze = deepcopy(maze)

            for _ in range(minutes):
                change = False
                fires = [[r, c] for r in range(rows) for c in range(cols) if new_maze[r][c] == 1]
                for r, c in fires:
                    for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                        if 0 <= nr < rows and 0 <= nc < cols and new_maze[nr][nc] == 0:
                            new_maze[nr][nc] = 1
                            change = True
                if not change:
                    break

            return new_maze

        # 1 - Test if we can reach at 0 - if not => -1
        if not has_path(0):
            return -1

        # 2 - Test if we can reach at m * n, and mark when/if no fire change - if no fire change before m * n then we have a 10**9 situation
        if has_path(rows * cols):
            return 10 ** 9

        low, high = 0, rows * cols
        while low < high:
            mid = (low + high + 1) // 2
            if has_path(mid):
                low = mid
            else:
                high = mid - 1
        return low

    # same idea but tighter
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        fires, visited = [], set()
        todo = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fires.append((row, col))
                    visited.add((row, col))
                    todo.append((row, col))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # If we stay for x minutes.
        def helper(minutes):
            fire, visited = fires[::], set()

            # Let the fire spreads for x minutes.
            while minutes > 0:
                new_fires = []
                for row, col in fire:
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                            # If the fire reach us before we move, we fail.
                            if nr == 0 and nc == 0:
                                return False
                            visited.add((nr, nc))
                            new_fires.append((nr, nc))
                fire = new_fires[::]
                minutes -= 1

            # Then let the fire and us move by turn (fire first).
            safe = [(0, 0)]
            while safe:
                # Fire spreads first.
                new_fires = []
                for row, col in fire:
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                            # If the fire reaches bot-right cell, if we are just one step close to bot-right cell
                            # We can still reach it, otherwise we fail. (Please refer to picture 2)
                            if nr == rows - 1 and nc == cols - 1:
                                if not ((rows - 2, cols - 1) in safe or (rows - 1, cols - 2) in safe):
                                    return False
                            visited.add((nr, nc))
                            new_fires.append((nr, nc))
                fire = new_fires[::]

                # We move then.
                newsafe = []
                for row, col in safe:
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        # If we can reach bot-right cell, success.
                        if nr == rows - 1 and nc == cols - 1:
                            return True
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            newsafe.append((nr, nc))
                safe = newsafe[::]

            # If there is no more cell for us to move before reaching bot-right cell, we fail.
            return False

        # check if always safe:
        while todo:
            row, col = todo.popleft()
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    todo.append((nr, nc))

        todo = deque([(0, 0)])
        while todo:
            row, col = todo.popleft()
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    if nr == rows - 1 and nc == cols - 1:
                        return 10 ** 9
                    visited.add((nr, nc))
                    todo.append((nr, nc))

        # Binary search to find maximum days:
        low, high = 0, 10 ** 4
        while low < high:
            mid = (low + high + 1) // 2
            if helper(mid):
                low = mid
            else:
                high = mid - 1

        return low if helper(low) else -1


solution = Solution()
assert solution.maximumMinutes([[0,0,0],[2,2,0],[1,2,0]]) == 1000000000
assert solution.maximumMinutes([[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]) == 3
assert solution.maximumMinutes([[0,0,0,0],[0,1,2,0],[0,2,0,0]]) == -1
