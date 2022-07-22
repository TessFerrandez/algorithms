from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre = -1 - k
        count = 0

        for num in nums:
            if num > pre + k:
                count += 1
                pre = num

        return count


solution = Solution()
assert solution.partitionArray([3, 6, 1, 2, 5], 2) == 2
assert solution.partitionArray([1, 2, 3], 1)
