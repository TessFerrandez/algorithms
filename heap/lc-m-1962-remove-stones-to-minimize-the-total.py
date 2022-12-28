from heapq import heapify, heappop, heappush
from math import ceil
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)

        for _ in range(k):
            largest = -heappop(piles)
            heappush(piles, -ceil(largest / 2))

        return 0 - sum(piles)


solution = Solution()
assert solution.minStoneSum([5, 4, 9], 2) == 12
assert solution.minStoneSum([4, 3, 6, 7], 3) == 12
