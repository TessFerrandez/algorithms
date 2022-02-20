'''
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.
'''
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        max_end = intervals[0][1]
        covered = 0

        for _, end in intervals[1:]:
            if end <= max_end:
                covered += 1
            else:
                max_end = end

        return len(intervals) - covered


solution = Solution()
assert solution.removeCoveredIntervals([[1, 5], [1, 3], [2, 5]]) == 1
assert solution.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]) == 2
assert solution.removeCoveredIntervals([[1, 4], [2, 3]]) == 1
