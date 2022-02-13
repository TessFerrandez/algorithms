'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
'''
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merged = []
        start, end = intervals[0]

        for start2, end2 in intervals:
            if start2 <= end:
                end = max(end, end2)
            else:
                merged.append([start, end])
                start, end = start2, end2

        merged.append([start, end])
        return merged


solution = Solution()
assert solution.insert([[1,3],[6,9]], [2, 5]) == [[1, 5], [6, 9]]
assert solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]) == [[1,2],[3,10],[12,16]]
