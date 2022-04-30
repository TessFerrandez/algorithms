from collections import deque
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    # Binary search + BFS
    # Time: O(m * n * log(max)) <- max absolute diff
    # Space: O(m * n)
    def minimumEffortPath1(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        target = (rows - 1, cols - 1)

        def isPath(effort: int) -> bool:
            visited, todo = {(0, 0)}, deque([(0, 0)])
            while todo:
                row, col = todo.popleft()
                if (row, col) == target:
                    return True
                for r, c in (row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col):
                    if 0 <= r < rows and 0 <= c < cols and abs(heights[r][c] - heights[row][col]) <= effort and (r, c) not in visited:
                        visited.add((r, c))
                        todo.append((r, c))
            return False

        min_height, max_height = min(min(row) for row in heights), max(max(row) for row in heights)

        low, high = 0, max_height - min_height
        while low < high:
            effort = (low + high) // 2
            if isPath(effort):
                high = effort
            else:
                low = effort + 1
        return low

    # Shortest fastest path
    # Time: O(m^2 * n^2)
    # Space: O(m * n)
    def minimumEffortPath2(self, heights: List[List[int]]) -> int:
        '''
        1. Initiate all efforts to MAX_INT except start which is 0
        2. Use BFS to traverse all reachable cells from start, updating efforts when we have a smaller value
        3. Repeat #2 until all efforts reach their minimum values
        4. Return the effort at end(m - 1, n - 1) as solution
        '''
        rows, cols = len(heights), len(heights[0])
        efforts = [[inf] * cols for _ in range(rows)]
        efforts[0][0] = 0

        todo = deque([(0, 0)])
        while todo:
            row, col = todo.popleft()
            for r, c in (row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col):
                if 0 <= r < rows and 0 <= c < cols:
                    next_effort = max(efforts[row][col], abs(heights[r][c] - heights[row][col]))
                    if efforts[r][c] > next_effort:
                        efforts[r][c] = next_effort
                        todo.append((r, c))

        return efforts[-1][-1]

    # Djikstra
    # Time: O(m * n * log(m * n))
    # Space: O(m * n)
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        target = (rows - 1, cols - 1)
        efforts = [[inf] * cols for _ in range(rows)]
        efforts[0][0] = 0

        todo = [(0, 0, 0)]
        while todo:
            effort, row, col = heappop(todo)
            print(effort, row, col)
            if (row, col) == target:
                return effort
            for r, c in (row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col):
                if 0 <= r < rows and 0 <= c < cols:
                    next_effort = max(efforts[row][col], abs(heights[r][c] - heights[row][col]))
                    if efforts[r][c] > next_effort:
                        efforts[r][c] = next_effort
                        heappush(todo, (next_effort, r, c))


solution = Solution()
assert solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]) == 2
assert solution.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]) == 1
assert solution.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0
