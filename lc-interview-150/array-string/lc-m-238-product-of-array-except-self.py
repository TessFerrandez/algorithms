# array, prefix sum
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current_prod = 1
        prefix = []
        for num in nums:
            prefix.append(current_prod)
            current_prod *= num

        current_prod = 1
        suffix = []
        for num in reversed(nums):
            suffix.append(current_prod)
            current_prod *= num

        suffix = list(reversed(suffix))
        return [prefix[i] * suffix[i] for i in range(len(nums))]


solution = Solution()
assert(solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
assert(solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])
assert(solution.productExceptSelf([0, 0]) == [0, 0])
