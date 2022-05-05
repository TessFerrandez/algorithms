'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for amount_left in range(1, amount + 1):
            dp[amount_left] = min([dp[amount_left - coin] if amount_left - coin >= 0 else float('inf') for coin in coins]) + 1

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

    # top down (template)
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def get_min_coins(amt):
            if amt < 0:
                return float('inf')
            if amt == 0:
                return 0
            if amt in coins:
                return 1
            options = [get_min_coins(amt - coin) for coin in coins]
            return min(options) + 1

        result = get_min_coins(amount)
        return -1 if result == float('inf') else result

    # bottom up (template)
    def coinChange2(self, coins: List[int], amount: int) -> int:
        min_coins = defaultdict(lambda: float('inf'))
        min_coins[0] = 0
        for coin in coins:
            min_coins[coin] = 1

        lowest_coin = min(coins)
        for amt in range(lowest_coin, amount + 1):
            for coin in coins:
                min_coins[amt] = min(min_coins[amt], min_coins[amt - coin] + 1)

        return -1 if min_coins[amount] == float('inf') else min_coins[amount]


solution = Solution()
assert solution.coinChange([1, 2, 5], 11) == 3
assert solution.coinChange([2], 3) == -1
assert solution.coinChange([1], 0) == 0
