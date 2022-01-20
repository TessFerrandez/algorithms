'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''
from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        lowest_speed = 10 ** 9

        while low <= high:
            current = (high - low) // 2 + low
            hours = sum(ceil(n / current) for n in piles)
            if hours > h:
                low = current + 1
            else:
                lowest_speed = min(lowest_speed, current)
                high = current - 1

        return lowest_speed


solution = Solution()
assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
