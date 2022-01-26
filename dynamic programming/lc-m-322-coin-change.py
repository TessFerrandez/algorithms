'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amount_left in range(1, amount + 1):
            dp[amount_left] = min([dp[amount_left - coin] if amount_left - coin >= 0 else float('inf') for coin in coins]) + 1

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]


solution = Solution()
assert solution.coinChange([1, 2, 5], 11) == 3
assert solution.coinChange([2], 3) == -1
assert solution.coinChange([1], 0) == 0
