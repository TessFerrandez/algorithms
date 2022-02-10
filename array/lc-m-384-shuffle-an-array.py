'''
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
'''
from typing import List
from random import randint


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


solution = Solution([1, 2, 3])
print(solution.shuffle())
print(solution.shuffle())
print(solution.shuffle())
print(solution.shuffle())
print(solution.shuffle())
print(solution.shuffle())
print(solution.reset())
