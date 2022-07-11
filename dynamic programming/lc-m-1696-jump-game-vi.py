from heapq import heappop, heappush
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        heap = [(-nums[-1], len(nums) - 1)]

        for i in range(len(nums) - 2, 0, -1):
            best, idx = heappop(heap)
            while idx > i + k:
                best, idx = heappop(heap)
            if idx != i + k:
                heappush(heap, (best, idx))
            heappush(heap, (-(nums[i] - best), i))

        best, idx = heappop(heap)
        while idx > k:
            best, idx = heappop(heap)
        return nums[0] - best


solution = Solution()
assert solution.maxResult([1], 2) == 1
assert solution.maxResult([1,-1,-2,4,-7,3], 2) == 7
assert solution.maxResult([10,-5,-2,4,0,3], 3) == 17
assert solution.maxResult([1,-5,-20,4,-1,3,-6,-3], 2) == 0
