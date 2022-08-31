from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        result = []
        for num in nums2:
            if num in nums1:
                result.append(num)
        return result


solution = Solution()
assert solution.intersection([1, 2, 2, 1], [2, 2]) == [2]
assert solution.intersection([4, 9, 5], [9, 4, 0, 8, 4]) == [9, 4]
