from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        lowest = []

        low_price = 10 ** 32
        for price in prices:
            low_price = min(low_price, price)
            lowest.append(low_price)

        max_profit = 0
        high_price = 0
        for i in range(len(prices) - 1, -1, -1):
            high_price = max(high_price, prices[i])
            max_profit = max(max_profit, high_price - lowest[i])

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < low:
                low = price
            else:
                max_profit = max(max_profit, price - low)

        return max_profit


solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
