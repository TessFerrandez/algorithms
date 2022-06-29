from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-num for num in target]
        heapify(heap)

        while True:
            item = -heappop(heap)
            total -= item
            if item == 1 or total == 1:
                return True
            if item < total or total == 0 or item % total == 0:
                return False
            item %= total
            total += item
            heappush(heap, -item)


solution = Solution()
assert solution.isPossible([9, 3, 5])
assert not solution.isPossible([1, 1, 1, 2])
assert solution.isPossible([8, 5])
