from collections import defaultdict
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        nums.sort()

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
                else:
                    break

        return dp[target]


solution = Solution()
assert solution.combinationSum4([1, 2, 3], 4) == 7
assert solution.combinationSum4([9], 3) == 0
