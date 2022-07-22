from itertools import groupby
from typing import List


class Solution:
    def countHillValley1(self, nums: List[int]) -> int:
        nums = [nums[i] for i in range(len(nums)) if i == 0 or i > 0 and nums[i] != nums[i - 1]]
        return sum(1 for i in range(1, len(nums) - 1) if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) or (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]))

    def countHillValley(self, nums: List[int]) -> int:
        nums = [num for num, _ in groupby(nums)]
        return sum(1 for i in range(1, len(nums) - 1) if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) or (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]))


solution = Solution()
assert solution.countHillValley([2, 4, 1, 1, 6, 5]) == 3
assert solution.countHillValley([6, 6, 5, 5, 4, 1]) == 0
