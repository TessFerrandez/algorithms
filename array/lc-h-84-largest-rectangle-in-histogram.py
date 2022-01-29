'''
Given an array of integers heights
representing the histogram's bar height
where the width of each bar is 1,
return the area of the largest rectangle
in the histogram.
'''
from typing import List


class Solution:
    # time limit exceeded
    def largestRectangleArea1(self, heights: List[int]) -> int:
        mins = []
        max_rect = 0

        for i, height in enumerate(heights):
            mins.append(height)
            for j in range(i + 1):
                if mins[j] > height:
                    mins[j] = height
                max_rect = max(max_rect, (i - j + 1) * mins[j])

        return max_rect

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        max_size = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_size = max(max_size, height * width)
            stack.append(i)

        return max_size


solution = Solution()
assert solution.largestRectangleArea([2, 1, 5, 6, 3, 2]) == 10
assert solution.largestRectangleArea([2, 4]) == 4
