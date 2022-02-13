'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        1. sort all intervals based on finish time ascending
        while intervals
            2. add the first available to scheduled
            3. remove all overlapping from intervals
        '''
        intervals = sorted(intervals, key=lambda x: x[1])

        _, end = intervals[0]
        scheduled = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                _, end = intervals[i]
                scheduled += 1

        return len(intervals) - scheduled


solution = Solution()
assert solution.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]) == 4
assert solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
assert solution.eraseOverlapIntervals([[1,2],[2,3]]) == 0
