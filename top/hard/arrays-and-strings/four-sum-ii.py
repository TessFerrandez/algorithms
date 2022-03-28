from collections import Counter
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count12 = Counter(n1 + n2 for n1 in nums1 for n2 in nums2)
        return sum(count12[-n3 - n4] for n3 in nums3 for n4 in nums4)


solution = Solution()
assert solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
assert solution.fourSumCount([0], [0], [0], [0]) == 1
