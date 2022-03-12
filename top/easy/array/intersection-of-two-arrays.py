from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)

        result = []
        for num in nums2:
            if num in c1 and c1[num] > 0:
                result.append(num)
                c1[num] -= 1

        return result


solution = Solution()
assert solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
assert solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
