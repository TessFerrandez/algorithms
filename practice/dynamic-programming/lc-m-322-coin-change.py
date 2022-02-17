from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        min_coins = [0 for _ in range(amount + 1)]

        for target in range(1, amount + 1):
            least = 10 ** 9
            for coin in coins:
                if target - coin >= 0:
                    least = min(least, min_coins[target - coin])
            min_coins[target] = 1 + least

        return -1 if min_coins[amount] >= 10 ** 9 else min_coins[amount]


solution = Solution()
assert solution.coinChange([1, 2, 5], 11) == 3
assert solution.coinChange([2], 3) == -1
assert solution.coinChange([1], 0) == 0
