'''
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.
'''
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds, evens = 0, 0

        for pos in position:
            if pos % 2 == 0:
                evens += 1
            else:
                odds += 1

        return min(odds, evens)


solution = Solution()
assert solution.minCostToMoveChips([1, 2, 3]) == 1
assert solution.minCostToMoveChips([2, 2, 2, 3, 3]) == 2
assert solution.minCostToMoveChips([1, 1000000000]) == 1
