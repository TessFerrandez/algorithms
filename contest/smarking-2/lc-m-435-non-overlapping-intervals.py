from cmath import inf
from typing import List


class Solution:
    '''
    can't sort by starts -- we will fail in this case [1, 100], [2, 3], [3, 4] -- so we need to sort by ends
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        current_end = -inf
        removed = 0

        for start, end in intervals:
            if start < current_end:
                removed += 1
            else:
                current_end = end

        return removed


solution = Solution()
assert solution.eraseOverlapIntervals([[-73,-26],[-65,-11],[-63,2],[-62,-49],[-52,31],[-40,-26],[-31,49],[30,47],[58,95],[66,98],[82,97],[95,99]]) == 7
assert solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
assert solution.eraseOverlapIntervals([[1,2],[2,3]]) == 0
assert solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]) == 0
