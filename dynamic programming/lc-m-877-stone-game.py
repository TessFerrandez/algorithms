'''
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.
'''
from typing import List


class Solution:
    # memo[(start, end)] contains the diff between Alice and Bob
    # A positive means Alice wins, negative means Bob wins
    def stoneGame1(self, piles: List[int]) -> bool:
        memo = {}
        def dp(start, end) -> int:
            if start > end:
                return 0

            if (start, end) not in memo:
                # player 1
                if (end - start) % 2 == 1:
                    memo[(start, end)] = max(piles[start] + dp(start + 1, end), dp(start, end - 1) + piles[end])
                # player 2
                else:
                    memo[(start, end)] = min(-piles[start] + dp(start + 1, end), dp(start, end - 1) + piles[end])

            return memo[(start, end)]

        return dp(0, len(piles) - 1) > 0

    # turns out - alice always wins
    def stoneGame(self, piles: List[int]) -> bool:
        return True


solution = Solution()
assert solution.stoneGame([5, 3, 4, 5]) == True
assert solution.stoneGame([3, 7, 2, 3]) == True
