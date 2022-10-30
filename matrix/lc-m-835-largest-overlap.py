from collections import defaultdict
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ones1 = [(row, col) for row in range(len(img1)) for col in range(len(img1[0])) if img1[row][col] == 1]
        ones2 = [(row, col) for row in range(len(img1)) for col in range(len(img1[0])) if img2[row][col] == 1]

        diffs = defaultdict(int)
        for x1, y1 in ones1:
            for x2, y2 in ones2:
                diffs[(x2 - x1, y2 - y1)] += 1

        if len(diffs.values()) == 0:
            return 0
        return max(diffs.values())


solution = Solution()
assert solution.largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]) == 3
assert solution.largestOverlap([[1]], [[1]]) == 1
assert solution.largestOverlap([[0]], [[0]]) == 0
