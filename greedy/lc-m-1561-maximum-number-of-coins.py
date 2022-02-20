'''
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.
'''
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        return sum(piles[1::2][:n])


solution = Solution()
assert solution.maxCoins([2, 4, 1, 2, 7, 8]) == 9
assert solution.maxCoins([2, 4, 5]) == 4
assert solution.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18
