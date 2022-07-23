from collections import defaultdict
from random import Random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)
        self.random = Random()

    def pick(self, target: int) -> int:
        indices = self.indices[target]
        idx = self.random.randint(0, len(indices) - 1)
        return indices[idx]


solution = Solution([1, 2, 3, 3, 3])
print(solution.pick(3))
print(solution.pick(1))
print(solution.pick(3))
