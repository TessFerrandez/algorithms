from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {coin: 1 for coin in coins}
        dp[0] = 0

        def min_coins(amount):
            if amount < 0:
                return -1

            if amount in dp:
                return dp[amount]

            possible = []
            for coin in coins:
                target = amount - coin
                num_coins = min_coins(target)
                if num_coins >= 0:
                    possible.append(num_coins)

            if possible:
                result = 1 + min(possible)
            else:
                result = -1
            dp[amount] = result
            return result

        return min_coins(amount)

    def coinChange2(self, coins: List[int], amount: int) -> int:
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
