from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right, merge = [], [], []

        for start, end in intervals:
            if end < newInterval[0]:
                left.append([start, end])
            elif start > newInterval[1]:
                right.append([start, end])
            else:
                merge.append([start, end])

        if not merge:
            merge = [newInterval]
        else:
            merge = [[min(merge[0][0], newInterval[0]), max(merge[-1][1], newInterval[1])]]

        return left + merge + right


solution = Solution()
assert solution.insert([[1,3],[6,9]], [2, 5]) == [[1,5],[6,9]]
assert solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
