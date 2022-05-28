from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid(divisor):
            return sum(ceil(num / divisor) for num in nums) <= threshold

        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if is_valid(mid):
                high = mid
            else:
                low = mid + 1
        return low


solution = Solution()
assert solution.smallestDivisor([1, 2, 5, 9], 6) == 5
assert solution.smallestDivisor([44, 22, 33, 11, 1], 5) == 44
