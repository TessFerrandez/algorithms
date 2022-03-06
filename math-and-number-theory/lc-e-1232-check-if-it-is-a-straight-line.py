'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane
'''
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        p1x, p1y = coordinates[0]
        p2x, p2y = coordinates[1]
        dxl, dyl = p2x - p1x, p2y - p1y

        for cx, cy in coordinates[2:]:
            dxc, dyc = cx - p1x, cy - p1y
            cross = dxc * dyl - dyc * dxl
            if cross != 0:
                return False
        return True


solution = Solution()
assert solution.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
assert not solution.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
