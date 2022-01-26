'''
Array - Greedy - Sorting

Given the width of some baloons (x1, x2) [[10,16],[2,8],[1,6],[7,12]]
Find the minimum amount of arrows that can be shot to shoot all baloons.
Here we can shoot one at 2, 3, 4, 5, or 6 (taking out [1, 6] and [2, 8])
and one at 10, 11, or 12 (taking out [7, 12] and [10, 16])

Solution:

1. Sort the intervals - this is our active balloons [[1,6],[2,8],[7,12],[10,16]]
2. Take the first one
3. Find all overlapping [1,6],[2,8] - and shoot an arrow at the min end (6) and remove all the shot baloons from active
4. Continue with #2

Since we don't need to know where to shoot - we can skip keeping track of the overlaps, we can just discard them
'''
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 0
        min_end = 10 ** 10

        for p1, p2 in points:
            if p1 > min_end:
                arrows += 1
                # print("shoot at", min_end)
                min_end = p2
            else:
                min_end = min(min_end, p2)

        if points:
            # print("shoot at", min_end)
            arrows += 1

        return arrows


solution = Solution()
assert solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
assert solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
assert solution.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2
assert solution.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]) == 2
