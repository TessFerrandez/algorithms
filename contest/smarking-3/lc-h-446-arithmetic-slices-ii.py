from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices1(self, nums: List[int]) -> int:
        n = len(nums)

        # (ends with index, diff)
        sequences = defaultdict(int)

        total_sequences = 0

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                sequences[(i, diff)] += sequences[(j, diff)] + 1
                total_sequences += sequences[(j, diff)]

        return total_sequences

    # better for mem
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        sequences = [defaultdict(int) for _ in range(n)]

        total = 0

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev_count = 0
                if diff in sequences[j]:
                    prev_count = sequences[j][diff]
                sequences[i][diff] += prev_count + 1
                total += prev_count

        return total


solution = Solution()
assert solution.numberOfArithmeticSlices([2,4,6,8,10]) == 7
assert solution.numberOfArithmeticSlices([7,7,7,7,7]) == 16
