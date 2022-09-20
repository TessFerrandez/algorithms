from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        max_profit = defaultdict(int)

        for trans in range(1, k + 1):
            min_buy_price = prices[0]
            for today in range(1, n):
                min_buy_price = min(min_buy_price, prices[today] - max_profit[(trans - 1, today - 1)])
                max_profit[(trans, today)] = max(max_profit[(trans, today - 1)], prices[today] - min_buy_price)

        return max_profit[(k, n - 1)]
