'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        n = len(nums2)

        for i, num in enumerate(nums2):
            hash_map[num] = i

        result = []

        for num in nums1:
            i = hash_map[num] + 1
            found = False
            while i < n and not found:
                if nums2[i] > num:
                    result.append(nums2[i])
                    found = True
                i += 1
            if not found:
                result.append(-1)

        return result


solution = Solution()
assert solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
assert solution.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
