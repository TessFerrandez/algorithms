from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        max_profit = 0

        for price in prices:
            lowest = min(lowest, price)
            max_profit = max(max_profit, price - lowest)

        return max_profit


solution = Solution()
assert solution.maxProfit([7,1,5,3,6,4]) == 5
assert solution.maxProfit([7,6,4,3,1]) == 0
