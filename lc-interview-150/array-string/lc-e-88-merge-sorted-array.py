# array, two pointers, sorting
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 or n > 0:
            if n == 0:
                break
            if m == 0 or nums1[m - 1] <= nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


solution = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
solution.merge(nums1, 3, nums2, 3)
assert(nums1 == [1, 2, 2, 3, 5, 6])

nums1 = [1]
nums2 = []
solution.merge(nums1, 1, nums2, 0)
assert(nums1 == [1])

nums1 = [0]
nums2 = [1]
solution.merge(nums1, 0, nums2, 1)
assert(nums1 == [1])
