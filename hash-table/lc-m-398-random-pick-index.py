'''
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
'''
from typing import List
from collections import defaultdict
from random import randint


class Solution:
    def __init__(self, nums: List[int]):
        self.num_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.num_map[num].append(i)

    def pick(self, target: int) -> int:
        i = randint(0, len(self.num_map[target]) - 1)
        return self.num_map[target][i]


solution = Solution([1, 2, 3, 3, 3])
print(solution.pick(3))
print(solution.pick(1))
print(solution.pick(3))