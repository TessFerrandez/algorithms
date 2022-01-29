'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

ALGO:
---------------
Always consider buying new stock
Sell when the price is higher
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = prices[0]

        for price in prices[1:]:
            if price > buy:
                result += price - buy
            buy = price

        return result


solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
