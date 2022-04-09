from heapq import heapify, heappop, heappush
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.hp = sorted(nums, reverse=True)[:k]
        self.k = k
        heapify(self.hp)

    def add(self, val: int) -> int:
        heappush(self.hp, val)
        if len(self.hp) > self.k:
            heappop(self.hp)
        return self.hp[0]


kth_largest = KthLargest(3, [4, 5, 8, 2])
assert kth_largest.add(3) == 4
assert kth_largest.add(5) == 5
assert kth_largest.add(10) == 5
assert kth_largest.add(9) == 8
assert kth_largest.add(4) == 8
