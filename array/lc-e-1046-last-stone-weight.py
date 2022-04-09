from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapify(neg_stones)

        while len(neg_stones) > 1:
            stone1 = -heappop(neg_stones)
            stone2 = -heappop(neg_stones)
            new_stone = stone1 - stone2
            if new_stone > 0:
                heappush(neg_stones, -new_stone)

        if len(neg_stones) == 1:
            return -neg_stones[0]
        else:
            return 0


solution = Solution()
assert solution.lastStoneWeight([2,7,4,1,8,1]) == 1
assert solution.lastStoneWeight([1]) == 1
