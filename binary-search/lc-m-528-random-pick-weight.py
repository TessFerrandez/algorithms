from bisect import bisect_left
import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.intervals = []
        total = sum(w)
        for weight in w:
            end = weight / total
            if not self.intervals:
                self.intervals.append(end)
            else:
                self.intervals.append(self.intervals[-1] + end)

    def pickIndex(self) -> int:
        r = random.random()
        return bisect_left(self.intervals, r)


solution = Solution([1, 3])
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
