from heapq import heappop, heappush
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(left, -height, right) for left, right, height in buildings] + list({(right, 0, None) for _, right, _ in buildings}))
        print(events)
        result, heap = [[0, 0]], [(0, float('inf'))]

        for left, neg_height, right in events:
            while left >= heap[0][1]:
                heappop(heap)
            if neg_height != 0:
                heappush(heap, (neg_height, right))
            if result[-1][1] + heap[0][0] != 0:
                result += [left, -heap[0][0]],

        return result[1:]


solution = Solution()
print(solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(solution.getSkyline([[0,2,3],[2,5,3]]))
