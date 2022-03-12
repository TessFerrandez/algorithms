from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = []
        lowest_price = 10 ** 32

        for price in prices:
            lowest_price = min(price, lowest_price)
            lowest.append(lowest_price)

        highest_price = 0
        max_profit = 0
        for i in range(len(prices) - 1, -1, -1):
            highest_price = max(highest_price, prices[i])
            max_profit = max(max_profit, highest_price - lowest[i])

        return max_profit


solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
