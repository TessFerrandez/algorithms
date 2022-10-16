from typing import List


class Solution:
    def maxScore(self, n: int, arr: List[int]) -> int:
        best = [0] * (10 ** 5 + 1)
        sorted_intervals = sorted(arr, reverse=True)

        max_so_far = 0
        latest = 10 ** 5

        for start, end, val in sorted_intervals:
            if max_so_far > 0:
                for i in range(latest - 1, start, -1):
                    best[i] = max_so_far
            latest = start
            current_best = val + best[end]
            best[start] = max(max(best[start], current_best), max_so_far)
            max_so_far = best[start]

        return max_so_far


solution = Solution()
assert solution.maxScore(6, [(4, 6, 7), (3, 6, 4), (2, 5, 4), (2, 6, 1), (1, 3, 9), (1, 3, 6)]) == 16
assert solution.maxScore(5, [(1,5,4), (1,3,10), (3,5,5), (1,2,1)]) == 15
assert solution.maxScore(5, [(1,5,4), (1,3,10), (3,5,5), (1,2,1), (2,3,2)]) == 15
assert solution.maxScore(2, [(1,2,10), (1,2,1)]) == 10
