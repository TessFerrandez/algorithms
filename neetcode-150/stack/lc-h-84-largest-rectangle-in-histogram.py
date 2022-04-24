from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        you can only make rectangles that are as high as one of the stacks
        - as soon as you reach a new stack, and it is shorter it can not be part
        of the rect of the prev. height

        ex. [2, 1, 5, 6, 2, 3]
        -1(0), 0(2), 1(1)
        - Pop 0(2) - area 2*1 = 2
        -1(0), 1(1), 2(5), 3(6), 4(2)
        - Pop 3(6) - area 6*1 = 6
        - Pop 2(5) - area 5*2 = 10 (BEST)
        -1(0), 1(1), 4(2), 5(3), 6(0) <- extra 0 at the end to finish all unfinished rects
        - Pop 5(3) - area 3*1 = 3
        - Pop 4(2) - area 2*2 = 4
        - Pop 1(1) - area 1*5 = 5
        '''
        stack, largest_rect = [-1], 0
        heights.append(0)

        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                largest_rect = max(largest_rect, h * w)
            stack.append(i)

        return largest_rect


solution = Solution()
assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
