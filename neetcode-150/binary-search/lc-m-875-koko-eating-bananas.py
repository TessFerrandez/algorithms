from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2
            hours = sum(ceil(pile / mid) for pile in piles)
            if hours <= h:
                high = mid
            else:
                low = mid + 1

        return high


solution = Solution()
assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
