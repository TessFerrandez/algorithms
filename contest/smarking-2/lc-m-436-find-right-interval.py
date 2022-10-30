from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_indices = {interval[0]: i for i, interval in enumerate(intervals)}
        starts = sorted(start_indices.keys())

        n = len(intervals)

        result = []
        for _, end in intervals:
            idx = bisect_left(starts, end)
            if idx >= n:
                result.append(-1)
            else:
                result.append(start_indices[starts[idx]])

        return result


solution = Solution()
assert solution.findRightInterval([[1,2]]) == [-1]
assert solution.findRightInterval([[3,4],[2,3],[1,2]]) == [-1, 0, 1]
assert solution.findRightInterval([[1,4],[2,3],[3,4]]) == [-1, 2, -1]
