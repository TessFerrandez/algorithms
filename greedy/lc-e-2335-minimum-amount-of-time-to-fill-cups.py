from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        cups = [-cup for cup in amount if cup != 0]
        heapify(cups)

        count = 0
        while cups:
            count += 1
            cup1 = heappop(cups)
            if cups:
                cup2 = heappop(cups)
                if cup2 + 1 < 0:
                    heappush(cups, cup2 + 1)
            if cup1 + 1 < 0:
                heappush(cups, cup1 + 1)

        return count


solution = Solution()
assert solution.fillCups([0, 0, 0]) == 0
assert solution.fillCups([1, 4, 2]) == 4
assert solution.fillCups([5, 4, 4]) == 7
assert solution.fillCups([5, 0, 0]) == 5
