class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def overlap(a1, a2, b1, b2):
            if b1 < a1:
                a1, a2, b1, b2 = b1, b2, a1, a2

            # rectangles don't overlap in this dimension
            # return 0, 0
            if a2 <= b1:
                return 0, 0

            # return the overlap region
            return b1, min(a2, b2)

        ox1, ox2 = overlap(ax1, ax2, bx1, bx2)
        oy1, oy2 = overlap(ay1, ay2, by1, by2)

        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        area_overlap = (ox2 - ox1) * (oy2 - oy1)

        return area_a + area_b - area_overlap


solution = Solution()
assert solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45
assert solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2) == 16
