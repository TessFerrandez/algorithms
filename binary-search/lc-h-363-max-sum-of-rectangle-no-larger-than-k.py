from bisect import bisect_left, insort
from itertools import accumulate, combinations, product
from math import inf
from typing import List
from sortedcontainers import SortedList


class Solution:
    # T: O(m^2*n log n) S: O(mn)
    def maxSumSubmatrix1(self, matrix: List[List[int]], k: int) -> int:
        def count_range_sum(nums, upper):
            # sorted prefix sums
            sorted_prefixes = SortedList([0])
            count = -inf

            for prefix in accumulate(nums):
                idx = sorted_prefixes.bisect_left(prefix - upper)
                if idx < len(sorted_prefixes):
                    count = max(count, prefix - sorted_prefixes[idx])
                sorted_prefixes.add(prefix)

            return count

        rows, cols, answer = len(matrix), len(matrix[0]), -inf

        for row, col in product(range(1, rows), range(cols)):
            matrix[row][col] += matrix[row - 1][col]

        matrix = [[0] * cols] + matrix

        for row1, row2 in combinations(range(rows + 1), 2):
            row = [j - i for i, j in zip(matrix[row1], matrix[row2])]
            answer = max(answer, count_range_sum(row, k))

        return answer

    # T: O(m^2*n^2) S: O(mn)
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def count_range_sum(nums, upper):
            # sorted prefix sums
            sorted_prefixes = [0]
            count = -inf

            for prefix in accumulate(nums):
                idx = bisect_left(sorted_prefixes, prefix - upper)
                if idx < len(sorted_prefixes):
                    count = max(count, prefix - sorted_prefixes[idx])
                insort(sorted_prefixes, prefix)

            return count

        rows, cols, answer = len(matrix), len(matrix[0]), -inf

        for row, col in product(range(1, rows), range(cols)):
            matrix[row][col] += matrix[row - 1][col]

        matrix = [[0] * cols] + matrix

        for row1, row2 in combinations(range(rows + 1), 2):
            row = [j - i for i, j in zip(matrix[row1], matrix[row2])]
            answer = max(answer, count_range_sum(row, k))

        return answer


solution = Solution()
assert solution.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2) == 2
assert solution.maxSumSubmatrix([[2,2,-1]], 3) == 3
