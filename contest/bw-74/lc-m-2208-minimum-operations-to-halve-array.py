from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapify(nums)

        whole_sum = sum(nums)
        half_sum = whole_sum / 2

        count = 0
        while whole_sum < half_sum:
            largest = heappop(nums)
            half = largest / 2
            heappush(nums, half)
            whole_sum += -1 * half
            count += 1

        return count


solution = Solution()
assert solution.halveArray([5, 19, 8, 1]) == 3
assert solution.halveArray([3, 8, 20]) == 3
