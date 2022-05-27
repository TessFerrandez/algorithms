from math import inf
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

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
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

    # binary search
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)

        low, high = 0, n2 * 2
        while low <= high:
            c2 = (low + high) // 2      # try cut c2
            c1 = n1 + n2 - c2           # calculate c1 based on c2

            left1 = -inf if (c1 == 0) else nums1[(c1 - 1) // 2]
            left2 = -inf if (c2 == 0) else nums2[(c2 - 1) // 2]
            right1 = inf if (c1 == n1 * 2) else nums1[c1 // 2]
            right2 = inf if (c2 == n1 * 2) else nums2[c2 // 2]

            if left1 > right2:
                low = c2 + 1        # num1s lower half too big, move c1 left (c2 right)
            elif left2 > right1:
                high = c2 - 1       # num2s lower half too big, move c2 left
            else:
                # we found it
                return (max(left1, left2) + min(right1, right2)) / 2

        return -1

    # divide and conquer
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kth(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]

            i1, i2 = len(nums1) // 2, len(nums2) // 2
            num1, num2 = nums1[i1], nums2[i2]

            print(nums1, nums2, k, i1, i2, num1, num2)

            # when k is bigger than the sum of num1 and num2s median indices
            if i1 + i2 < k:
                # if num1s median is bigger than num2s, num2s first half doesn't include k
                if num1 > num2:
                    return kth(nums1, nums2[i1 + 1:], k - i2 - 1)
                else:
                    return kth(nums1[i1 + 1:], nums2, k - i1 - 1)

            # when k is smaller than the sum of num1 and num2s indices
            else:
                # if num1s median is bigger than num2s, num1s second half doesn't include k
                if num1 > num2:
                    return kth(nums1[: i1], nums2, k)
                else:
                    return kth(nums1, nums2[: i2], k)

        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return kth(nums1, nums2, n // 2)
        else:
            return (kth(nums1, nums2, n // 2) + kth(nums1, nums2, n // 2 - 1)) / 2


solution = Solution()
assert solution.findMedianSortedArrays([1, 2, 3, 4, 5], [1, 1, 1, 1]) == 1
assert solution.findMedianSortedArrays([1, 3], [2]) == 2
assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
