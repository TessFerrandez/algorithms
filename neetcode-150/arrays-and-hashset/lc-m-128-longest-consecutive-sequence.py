from functools import cache
from typing import List


class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        lookup = {}

        for i, num in enumerate(nums):
            lookup[num] = i

        parents = [-1 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            if num - 1 in lookup:
                parents[i] = lookup[num - 1]

        @cache
        def get_len(i):
            if parents[i] == -1:
                return 1
            return 1 + get_len(parents[i])

        max_len = 0
        for i, parent in enumerate(parents):
            if parent == -1:
                length = 1
            else:
                length = 1 + get_len(parent)
            max_len = max(max_len, length)

        return max_len

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            # start of a sequence
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(length, longest)

        return longest


solution = Solution()
assert solution.longestConsecutive([]) == 0
assert solution.longestConsecutive([0]) == 1
assert solution.longestConsecutive([0, 0]) == 1
assert solution.longestConsecutive([100,4,200,1,3,2]) == 4
assert solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
