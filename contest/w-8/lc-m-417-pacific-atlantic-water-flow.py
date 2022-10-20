from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ATLANTIC, PACIFIC = 0, 1
        rows, cols = len(heights), len(heights[0])

        def is_atlantic(row, col):
            return row == 0 or col == 0

        def is_pacific(row, col):
            return row == rows - 1 or col == cols - 1

        def is_in_bounds(row, col):
            return 0 <= row < rows and 0 <= col < cols

        # dfs
        def can_reach(row, col, ocean):
            if ocean == ATLANTIC and is_atlantic(row, col):
                return True
            if ocean == PACIFIC and is_pacific(row, col):
                return True

            self.visited.add((row, col))

            height = heights[row][col]
            for nrow, ncol in (row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col):
                if is_in_bounds(nrow, ncol) and (nrow, ncol) not in self.visited and heights[nrow][ncol] <= height and can_reach(nrow, ncol, ocean):
                    return True

            return False

        result = []

        for row in range(rows):
            for col in range(cols):
                self.visited = set()
                if can_reach(row, col, ATLANTIC):
                    self.visited = set()
                    if can_reach(row, col, PACIFIC):
                        result.append([row, col])

        return result


solution = Solution()
assert solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
assert solution.pacificAtlantic([[1]]) == [[0, 0]]
