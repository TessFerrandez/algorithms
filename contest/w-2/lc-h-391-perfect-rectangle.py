from collections import defaultdict
from math import inf
from typing import List

class Solution:
    # doesn't take care of overlaps
    # ex. [[0,0,1,1],[0,1,3,2],[1,0,2,2]]
    def isRectangleCover1(self, rectangles: List[List[int]]) -> bool:
        miny, minx, maxy, maxx = inf, inf, -inf, -inf

        total_area = 0
        for y1, x1, y2, x2 in rectangles:
            miny = min(miny, y1)
            minx = min(minx, x1)
            maxy = max(maxy, y2)
            maxx = max(maxx, x2)

            total_area += (y2 - y1) * (x2 - x1)

        big_area = (maxy - miny) * (maxx - minx)
        return big_area == total_area

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        '''
        - The 4 corners of the big rectangle (outer) - occur once and only once among the sub-rectangles
        - T-junctions - occur twice among the sub-rectangles
        - Crosses - occur four times among sub-rectangles
        - A point can only be the top-left corner of at most one sub-rectangle - otherwise we have an overlap
          Same for top-right, bottom-left, bottom-right
        '''
        BOTTOM_LEFT = 1
        BOTTOM_RIGHT = 2
        TOP_LEFT = 4
        TOP_RIGHT = 8

        def insert_corner(x, y, val):
            if (x, y) in corner_map and corner_map[(x, y)] & val:
                return False
            corner_map[(x, y)] |= val
            return True

        minx = maxx = rectangles[0][0]
        miny = maxy = rectangles[0][1]

        corner_map = defaultdict(int)

        for lx, by, rx, ty in rectangles:
            minx, maxx = min(minx, lx), max(maxx, rx)
            miny, maxy = min(miny, by), max(maxy, ty)
            if not insert_corner(lx, by, BOTTOM_LEFT):
                return False
            if not insert_corner(rx, by, BOTTOM_RIGHT):
                return False
            if not insert_corner(lx, ty, TOP_LEFT):
                return False
            if not insert_corner(rx, ty, TOP_RIGHT):
                return False

        valid_corner = {BOTTOM_LEFT, BOTTOM_RIGHT, TOP_LEFT, TOP_RIGHT}
        valid_interior = {BOTTOM_LEFT + BOTTOM_RIGHT, BOTTOM_LEFT + TOP_LEFT, BOTTOM_RIGHT + TOP_RIGHT, TOP_LEFT + TOP_RIGHT, BOTTOM_LEFT + BOTTOM_RIGHT + TOP_LEFT + TOP_RIGHT}

        for x, y in corner_map:
            if x in (minx, maxx) and y in (miny, maxy):
                if corner_map[(x, y)] not in valid_corner:
                    return False
            else:
                if corner_map[(x, y)] not in valid_interior:
                    return False

        return True


solution = Solution()
assert solution.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
assert not solution.isRectangleCover([[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]])
assert not solution.isRectangleCover([[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]])
assert not solution.isRectangleCover([[0,0,1,1],[0,1,3,2],[1,0,2,2]])
