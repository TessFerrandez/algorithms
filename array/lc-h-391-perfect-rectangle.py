'''
Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

Return true if all the rectangles together form an exact cover of a rectangular region.
'''
from typing import List
from collections import defaultdict

class Solution:
    # takes too long
    def isRectangleCover1(self, rectangles: List[List[int]]) -> bool:
        def overlaps(rect1, rect2):
            # if one of the rects are a line, we don't have overlap
            if rect1[0] == rect1[2] or rect1[1] == rect1[3] or rect2[0] == rect2[2] or rect2[1] == rect2[3]:
                return False
            # one rect is to the left of the other
            if rect1[0] >= rect2[2] or rect2[0] >= rect1[2]:
                return False
            # one rect is above the other
            if rect1[1] >= rect2[3] or rect2[1] >= rect1[3]:
                return False

            return True

        def calc_area(x1, y1, x2, y2):
            return (y2 - y1) * (x2 - x1)

        def get_outer_corners():
            x1 = min(x1 for x1, _, _, _ in rectangles)
            x2 = max(x2 for _, _, x2, _ in rectangles)
            y1 = min(y1 for _, y1, _, _ in rectangles)
            y2 = max(y2 for _, _, _, y2 in rectangles)
            return x1, y1, x2, y2

        sum_rect_areas = sum(calc_area(x1, y1, x2, y2) for x1, y1, x2, y2 in rectangles)

        x1, y1, x2, y2 = get_outer_corners()
        big_rect_area = calc_area(x1, y1, x2, y2)

        if big_rect_area != sum_rect_areas:
            return False

        added_rects = []
        for rect in rectangles:
            for rect2 in added_rects:
                if overlaps(rect, rect2):
                    return False
            added_rects.append(rect)

        return True

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        '''
        1. Area of total must be same as area of sub rectangles
        2. External corners must appear only once
        3. Internal corners appear 2 or 4 times
        '''
        corners = defaultdict(int)
        ox1, oy1, ox2, oy2, area = float('inf'), float('inf'), -float('inf'), -float('inf'), 0

        for x1, y1, x2, y2 in rectangles:
            ox1, oy1, ox2, oy2 = min(ox1, x1), min(oy1, y1), max(ox2, x2), max(oy2, y2)
            area += (x2 - x1) * (y2 - y1)
            for corner in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                corners[corner] += 1

        if area != (oy2 - oy1) * (ox2 - ox1):
            return False

        outer = {(ox1, oy1), (ox2, oy2), (ox1, oy2), (ox2, oy1)}

        odd_corners = {corner for corner in corners if corners[corner] % 2}
        single_corners = {corner for corner in corners if corners[corner] == 1}

        if single_corners != outer or odd_corners != single_corners:
            return False

        return True

    def isRectangleCover2(self, rectangles: List[List[int]]) -> bool:
        '''
        1. Area of total must be same as area of sub rectangles
        2. External corners must appear only once
        3. Internal corners appear 2 or 4 times

        Same as above but filtered with xor
        '''
        area = 0
        corners = set()
        get_area = lambda: (y1 - y2) * (x1 - x2)

        for x1, y1, x2, y2 in rectangles:
            area += get_area()
            corners ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}

        if len(corners) != 4:
            return False

        x1, y1 = min(corners, key=lambda x: x[0] + x[1])
        x2, y2 = max(corners, key=lambda x: x[0] + x[1])
        return get_area() == area


solution = Solution()
assert solution.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]) == True
assert solution.isRectangleCover([[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]) == False
assert solution.isRectangleCover([[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]) == False
