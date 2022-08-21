from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])

        result = []
        for row in range(rows - 2):
            result.append([])
            for col in range(cols - 2):
                max_val = 0
                for dr in range(3):
                    for dc in range(3):
                        max_val = max(max_val, grid[row + dr][col + dc])
                result[-1].append(max_val)
        return result


solution = Solution()
assert solution.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]) == [[9, 9], [8, 6]]
assert solution.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
