from collections import defaultdict
from typing import List

'''
Key insight:
1. Instead of counting bad pairs, we can count all pairs and good pairs
2. j - i = nums[j] - nums[i] =>
   j - nums[j] = i - nums[i]
so our sets of good pairs have the same diffs of index - num[index]
'''
class Solution:
    def countBadPairs1(self, nums: List[int]) -> int:
        n = len(nums)
        all_pairs = n * (n - 1) // 2

        count_diffs = defaultdict(int)
        for i in range(n):
            count_diffs[i - nums[i]] += 1

        good_pairs = 0
        for diff in count_diffs:
            good_pairs += count_diffs[diff] * (count_diffs[diff] - 1) // 2

        return all_pairs - good_pairs

    # maybe cleaner
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        all = n * (n - 1) // 2
        good = 0
        dp = defaultdict(int)

        for i, num in enumerate(nums):
            v = i - num
            good += dp[v]
            dp[v] += 1

        return all - good


solution = Solution()
assert solution.countBadPairs([4,1,3,3]) == 5
assert solution.countBadPairs([1,2,3,4,5]) == 0
assert solution.countBadPairs([4,1,3,3,4,6,6,8,7]) == 27
assert solution.countBadPairs([4,1,3,3,4,6,6,8,8]) == 23
