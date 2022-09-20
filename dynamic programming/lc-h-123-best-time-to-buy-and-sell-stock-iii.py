from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        max_profit = defaultdict(int)

        for k in range(1, 2 + 1):
            for today in range(1, n):
                max_profit_if_sell = 0
                for buy in range(today):
                    max_profit_if_sell = max(max_profit_if_sell, prices[today] - prices[buy] + max_profit[(k - 1, buy - 1)])
                max_profit[(k, today)] = max(max_profit[(k - 1, today)], max_profit_if_sell)

        return max_profit[(2, n - 1)]

    # optimized
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        max_profit = defaultdict(int)

        for k in range(1, 2 + 1):
            min_buy_price = prices[0]
            for today in range(1, n):
                min_buy_price = min(min_buy_price, prices[today] - max_profit[(k - 1, today - 1)])
                max_profit[(k, today)] = max(max_profit[(k, today - 1)], prices[today] - min_buy_price)

        return max_profit[(2, n - 1)]

    # since k == 2
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = inf, inf
        sell1, sell2 = 0, 0

        for today in range(len(prices)):
            buy1 = min(buy1, prices[today])
            sell1 = max(sell1, prices[today] - buy1)
            buy2 = min(buy2, prices[today] - sell1)
            sell2 = max(sell2, prices[today] - buy2)

        return sell2


solution = Solution()
assert solution.maxProfit([3,3,5,0,0,3,1,4]) == 6
assert solution.maxProfit([1,2,3,4,5]) == 4
