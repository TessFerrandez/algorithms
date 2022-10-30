from typing import Counter, List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count_12sums = Counter(n1 + n2 for n1 in nums1 for n2 in nums2)
        zero_sums = sum(count_12sums[-n3 - n4] for n3 in nums3 for n4 in nums4)
        return zero_sums


solution = Solution()
assert solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
assert solution.fourSumCount([0], [0], [0], [0]) == 1
