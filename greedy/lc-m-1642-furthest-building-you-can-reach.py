from heapq import heappop, heappush
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)

        for i in range(n - 1):
            climb = heights[i + 1] - heights[i]

            # this is not an upwards climb
            if climb <= 0:
                continue

            if climb > 0:
                heappush(heap, climb)

            # we have used up all the ladders
            if len(heap) > ladders:
                # find the shortest climb and use bricks there
                brick_need = heappop(heap)
                bricks -= brick_need

            if bricks < 0:
                return i

        return n - 1


solution = Solution()
assert solution.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4
assert solution.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7
assert solution.furthestBuilding([14, 3, 19, 3], 17, 0) == 3
