from random import randint
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len = len(nums)

    def reset(self) -> List[int]:
        return self.nums[::]

    def shuffle(self) -> List[int]:
        shuffled = self.nums[::]

        for i in range(self.len):
            pos = randint(0, self.len - 1)
            shuffled[i], shuffled[pos] = shuffled[pos], shuffled[i]

        return shuffled
