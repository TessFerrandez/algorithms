from typing import List, Tuple


def get_next(nums1, nums2, l1i, l2i) -> Tuple[int, int, int]:
    if l1i >= len(nums1):
        return nums2[l2i], l1i, l2i + 1
    if l2i >= len(nums2):
        return nums1[l1i], l1i + 1, l2i
    if nums1[l1i] <= nums2[l2i]:
        return nums1[l1i], l1i + 1, l2i
    else:
        return nums2[l2i], l1i, l2i + 1


class Solution:
    def findMedianSortedArrays_try1(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        odd = True
        mid = total_len // 2

        if total_len % 2 == 0:
            odd = False

        num, l1i, l2i = 0, 0, 0
        for _ in range(mid):
            num, l1i, l2i = get_next(nums1, nums2, l1i, l2i)
        if odd:
            num, l1i, l2i = get_next(nums1, nums2, l1i, l2i)
            return num
        else:
            num2, l1i, l2i = get_next(nums1, nums2, l1i, l2i)
            return (num + num2) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        odd = total_len % 2
        mid = total_len // 2

        combined = []
        i1, i2 = 0, 0

        while i1 + i2 <= mid and i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                combined.append(nums1[i1])
                i1 += 1
            else:
                combined.append(nums2[i2])
                i2 += 1

        if i1 + i2 <= mid:
            if i1 < len(nums1):
                combined += nums1[i1: i1 + mid - i2 + 1]
            else:
                combined += nums2[i2: i2 + mid - i1 + 1]

        return float(combined[mid] if odd else (combined[mid - 1] + combined[mid]) / 2)


solution = Solution()
assert solution.findMedianSortedArrays([1, 3], [2]) == 2
assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
