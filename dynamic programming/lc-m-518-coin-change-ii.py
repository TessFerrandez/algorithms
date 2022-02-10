'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
'''
from typing import List
from collections import defaultdict


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combinations = defaultdict(int)
        combinations[0] = 1

        for coin in coins:
            for amt in range(1, amount + 1):
                if amt - coin >= 0:
                    combinations[amt] += combinations[amt - coin]

        return combinations[amount]


solution = Solution()
assert solution.change(5, [1, 2, 5]) == 4
assert solution.change(3, [2]) == 0
assert solution.change(10, [10]) == 1
