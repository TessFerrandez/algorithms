from collections import defaultdict
from typing import List


class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        majority = len(nums) // 2 + 1

        for num in nums:
            counts[num] += 1
            if counts[num] == majority:
                return num

    # T O(n) S O(1) - Boyer Moore
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


solution = Solution()
assert solution.majorityElement([3, 2, 3])
assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2])
