'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

ALGO:
-------------
We have 3 actions at each position, we can wait, buy or sell

WAIT, BUY, SELL

WAIT -> Wait -> WAIT
WAIT -> Buy -> BUY - price of stock

BUY -> Buy -> BUY
BUY -> Sell -> Sell + price of stock

SELL -> Wait -> WAIT

Our biggest profit is made either in the SELL state or WAIT state, as in the BUY state we have unsold stock
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        wait = [0] * n
        sell = [0] * n
        buy = [0] * n
        buy[0] = -prices[0]
        sell[0] = -float('inf')

        for i in range(1, n):
            wait[i] = max(wait[i - 1], sell[i - 1])
            buy[i] = max(wait[i - 1] - prices[i], buy[i - 1])
            sell[i] = buy[i - 1] + prices[i]

        return max(max(wait), max(sell))


solution = Solution()
assert solution.maxProfit([1, 2, 3, 0, 2]) == 3
assert solution.maxProfit([1]) == 0
