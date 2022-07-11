from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far, max_profit = inf, 0

        for price in prices:
            max_profit = max(max_profit, price - min_so_far)
            min_so_far = min(min_so_far, price)

        return max_profit


solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
