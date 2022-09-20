from collections import defaultdict
from typing import List


class Solution:
    # TlE
    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:
        indices = defaultdict(list)
        max_length = 0
        cache = defaultdict(int)

        for i, num in enumerate(nums2):
            indices[num].append(i)

        for i in range(len(nums1) - 1, -1, -1):
            num = nums1[i]
            for idx in indices[num]:
                length = 1 + cache[(i + 1, idx + 1)]
                max_length = max(max_length, length)
                cache[(i, idx)] = length

        return max_length

    def findLength2(self, nums1: List[int], nums2: List[int]) -> int:
        cache = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    cache[i][j] = cache[i + 1][j + 1] + 1

        return max(max(row) for row in cache)

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        indices = defaultdict(list)
        cache = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for i, num in enumerate(nums2):
            indices[num].append(i)

        for i in range(len(nums1) - 1, -1, -1):
            num = nums1[i]
            for j in indices[num]:
                cache[i][j] = 1 + cache[i + 1][j + 1]

        return max(max(row) for row in cache)


solution = Solution()
assert solution.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
assert solution.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5
