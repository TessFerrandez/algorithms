from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
