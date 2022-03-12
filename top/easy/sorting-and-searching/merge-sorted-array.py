from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        current = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[current] = nums1[m - 1]
                m -= 1
            else:
                nums1[current] = nums2[n - 1]
                n -= 1
            current -= 1

        while n > 0:
            nums1[current] = nums2[n - 1]
            n -= 1
            current -= 1


solution = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
solution.merge(nums1, 3, [2, 5, 6], 3)
assert nums1 == [1, 2, 2, 3, 5, 6]

nums1 = [1]
solution.merge(nums1, 1, [], 0)
assert nums1 == [1]

nums1 = [0]
solution.merge(nums1, 0, [1], 1)
assert nums1 == [1]
