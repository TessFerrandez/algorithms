from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]


solution = Solution()
assert solution.findDifference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]]
assert solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2]) == [[3], []]
