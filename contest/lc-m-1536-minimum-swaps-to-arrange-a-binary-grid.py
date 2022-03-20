from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def get_rightmost_one(row):
            for i in range(n - 1, -1, -1):
                if row[i] == 1:
                    return i
            return -1

        def solution_is_possible(max_right):
            sorted_right = list(sorted(max_right))

            for pos, val in enumerate(sorted_right):
                if val > pos:
                    return False
            return True

        max_right = [get_rightmost_one(row) for row in grid]
        if not solution_is_possible(max_right):
            return -1

        swaps = 0
        for pos in range(n):
            idx = 0
            while max_right[idx] > pos:
                idx += 1

            max_right = max_right[:idx] + max_right[idx + 1:]
            swaps += idx

        return swaps


solution = Solution()
assert solution.minSwaps([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]) == -1
assert solution.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]) == 3
assert solution.minSwaps([[1, 0, 0], [1, 1, 0], [1, 1, 1]]) == 0
