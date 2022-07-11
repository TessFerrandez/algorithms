from heapq import heappop, heappush
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heappush(heap, (sqrt(x ** 2 + y ** 2), x, y))

        result = []
        for _ in range(k):
            _, x, y = heappop(heap)
            result.append([x, y])

        return result


solution = Solution()
assert solution.kClosest([[1,3],[-2,2]], 1) == [[-2, 2]]
assert solution.kClosest([[3,3],[5,-1],[-2,4]], 2) == [[3,3],[-2,4]]
