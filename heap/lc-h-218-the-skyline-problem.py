from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    '''
    scan all (x, height) points from left to right, if max height changes, record it in the final result
    to know the max height at any x position, we keep a max-heap record (height, x)
    ex. in example 1 - (5, 12) should not be in the final result as for x=5, the max height is 15
    '''
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # for the same x (x, -H) should be in front of (x, 0)
        # ex. for example 2, we should process (2, -3) and then (2, 0) as there is no height change
        x_height_rights = sorted([(left, -height, right) for left, right, height in buildings] + [(right, 0, 0) for _, right, _ in buildings])

        # (0, inf) is always in max_heap so max_heap[0] is always valid
        result, max_heap = [[0, 0]], [(0, inf)]

        for x, negative_height, right in x_height_rights:
            while x >= max_heap[0][1]:
                # reduce max height up to date, i.e. only consider max height on the right side of line x
                heappop(max_heap)
            if negative_height:
                # consider each height, as it may be the potential max height
                heappush(max_heap, (negative_height, right))
            curr_max_height = -max_heap[0][0]
            if result[-1][1] != curr_max_height:
                result.append([x, curr_max_height])

        return result[1:]


solution = Solution()
print(solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(solution.getSkyline([[0,2,3],[2,5,3]]))
