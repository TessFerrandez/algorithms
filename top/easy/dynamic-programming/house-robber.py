from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_loot = {-1: 0, -2: 0}

        for i in range(n):
            max_loot[i] = max(nums[i] + max_loot[i - 2], max_loot[i - 1])

        return max_loot[n - 1]


solution = Solution()
assert solution.rob([1, 2, 3, 1]) == 4
assert solution.rob([2, 7, 9, 3, 1]) == 12
