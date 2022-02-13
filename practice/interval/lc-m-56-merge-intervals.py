from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
assert solution.merge([[1, 4], [0, 4]]) == [[0, 4]]
assert solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
