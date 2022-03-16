from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []

        start, end = intervals[0]
        for current_start, current_end in intervals[1:]:
            if current_start <= end:
                end = max(current_end, end)
            else:
                merged.append([start, end])
                start, end = current_start, current_end

        merged.append([start, end])
        return merged


solution = Solution()
assert solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert solution.merge([[1,4],[4,5]]) == [[1, 5]]
