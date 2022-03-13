'''
You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.
'''
from typing import List


class Solution:
    def findKDistantIndices1(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = []
        for i, num in enumerate(nums):
            if num == key:
                keys.append(i)

        n = len(nums)
        kdistant = set()
        for key in keys:
            for i in range(max(key - k, 0), min(key + k + 1, n)):
                kdistant.add(i)

        return list(kdistant)

    # better
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        kdistant = set()

        for i, num in enumerate(nums):
            if num == key:
                for j in range(max(i - k, 0), min(i + k + 1, n)):
                    kdistant.add(j)

        return list(kdistant)


solution = Solution()
assert solution.findKDistantIndices([2,2,2,2,2], 2, 2) == [0, 1, 2, 3, 4]
assert solution.findKDistantIndices([3,4,9,1,3,9,5], 9, 1) == [1,2,3,4,5,6]
