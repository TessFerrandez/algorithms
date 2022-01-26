'''
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.
'''
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)    # inventory high to low
        inventory.append(0)

        profit = 0
        k = 1

        for i in range(len(inventory) - 1):
            if inventory[i] > inventory[i + 1]:
                if k * (inventory[i] - inventory[i + 1]) < orders:
                    profit += k * (inventory[i] + inventory[i + 1] + 1) * (inventory[i] - inventory[i + 1]) // 2    # arithmic sum
                    orders -= k * (inventory[i] - inventory[i + 1])
                else:
                    q, r = divmod(orders, k)
                    profit += k * (2 * inventory[i] - q + 1) * q // 2 + r * (inventory[i] - q)
                    return profit % 1_000_000_007
            k += 1


solution = Solution()
assert solution.maxProfit([2, 5], 4) == 14
assert solution.maxProfit([3, 5], 6) == 19
