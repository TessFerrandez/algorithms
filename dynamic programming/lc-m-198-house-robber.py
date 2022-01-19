'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
from typing import List, Tuple
from functools import lru_cache


class Solution:
    # recursive
    def rob1(self, nums: List[int]) -> int:
        def rob_recursive(nums: List[int], i: int) -> int:
            if i < 0:
                return 0
            return max(rob_recursive(nums, i - 2) + nums[i], rob_recursive(nums, i - 1))

        return rob_recursive(nums, len(nums) - 1)

    # recursive + memo
    def rob2(self, nums: List[int]) -> int:
        cache = [-1 for _ in range(len(nums))]

        def rob_recursive(nums: List[int], i: int) -> int:
            if i < 0:
                return 0

            if cache[i] == -1:
                cache[i] = max(rob_recursive(nums, i - 2) + nums[i], rob_recursive(nums, i - 1))

            return cache[i]

        return rob_recursive(nums, len(nums) - 1)


    # iterative + memo
    def rob3(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # one based to allow for i-2 which now becomes i - 1
        cache = [0 for _ in range(len(nums) + 1)]

        cache[0] = 0
        cache[1] = nums[0]

        for i, num in enumerate(nums):
            cache[i + 1] = max(cache[i - 1] + num, cache[i])

        return cache[len(nums)]


    # iterative + memo (less space)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # one based to allow for i-2 which now becomes i - 1
        prev1, prev2 = 0, 0

        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1

        return prev1


solution = Solution()
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))
print(solution.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
