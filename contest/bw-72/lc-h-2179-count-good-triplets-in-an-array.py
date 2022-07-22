'''
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.
'''
from typing import List


class Solution:
    # TLE
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        indices = {nums2[i]: i for i in range(n)}

        good_triplets = 0
        for i in range(n - 2):
            idx_i = indices[nums1[i]]
            for j in range(i + 1, n - 1):
                idx_j = indices[nums1[j]]
                if idx_i < idx_j:
                    for k in range(j + 1, n):
                        idx_k = indices[nums1[k]]
                        if idx_k > idx_j:
                            good_triplets += 1

        return good_triplets


solution = Solution()
assert solution.goodTriplets([2, 0, 1, 3], [0, 1, 2, 3]) == 1
assert solution.goodTriplets([4, 0, 1, 3, 2], [4, 1, 0, 2, 3]) == 4
