# array, dynamic programming
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price

        return profit


solution = Solution()
assert(solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
assert(solution.maxProfit([7, 6, 4, 3, 1]) == 0)
