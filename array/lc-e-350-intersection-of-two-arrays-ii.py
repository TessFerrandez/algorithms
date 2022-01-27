from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = Counter(nums1), Counter(nums2)

        result = []
        for num in n1:
            freq = min(n1[num], n2[num]) if num in n2 else 0
            for _ in range(freq):
                result.append(num)

        return result


solution = Solution()
assert solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
assert solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
