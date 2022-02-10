'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        merged = []

        start, end = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                merged.append([start, end])
                start, end = interval

        merged.append([start, end])
        return merged


solution = Solution()
assert solution.merge([[2, 6], [1, 3], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
