from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def get_change(amount_left):
            if amount_left == 0:
                return 0

            coins_used = []
            for coin in coins:
                if coin <= amount_left:
                    n_coins = get_change(amount_left - coin)
                    if n_coins != -1:
                        coins_used.append(1 + n_coins)

            if coins_used:
                return min(coins_used)
            else:
                return -1

        return get_change(amount)


solution = Solution()
assert solution.coinChange([1, 2, 5], 11) == 3
assert solution.coinChange([2], 3) == -1
assert solution.coinChange([1], 0) == 0
