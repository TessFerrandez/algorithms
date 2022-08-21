from math import ceil
from typing import List


class Solution:
    # my solution during contest - slightly wrong
    def minimumReplacement1(self, nums: List[int]) -> int:
        min_val = nums[-1]
        count = 0
        for i in range(len(nums) - 1)[::-1]:
            if nums[i] > min_val:
                count += ceil(nums[i] / min_val) - 1
                if nums[i] % min_val != 0:
                    min_val = nums[i] % min_val
            min_val = min(min_val, nums[i])

        return count

    # correct solution
    def minimumReplacement(self, nums: List[int]) -> int:
        min_val = nums[-1]
        splits = 0

        for i in range(len(nums) - 1)[::-1]:
            min_splits = ceil(nums[i] / min_val)
            splits += min_splits - 1
            min_val = nums[i] // min_splits

        return splits


solution = Solution()
assert solution.minimumReplacement([19,7,2,24,11,16,1,11,23]) == 73
assert solution.minimumReplacement([3, 4, 5, 3]) == 3
assert solution.minimumReplacement([3, 9, 3]) == 2
assert solution.minimumReplacement([1, 2, 3, 4, 5]) == 0
assert solution.minimumReplacement([12,9,7,6,17,19,21]) == 6
