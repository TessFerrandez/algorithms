from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        half = n // 2

        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count[num] > half:
                return num


solution = Solution()
assert solution.majorityElement([3, 2, 3]) == 3
assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
