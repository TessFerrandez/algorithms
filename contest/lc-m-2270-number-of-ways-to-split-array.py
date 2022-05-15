from itertools import accumulate
from typing import List


class Solution:
    # my solution
    def waysToSplitArray1(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        postfix = list(accumulate(nums[::-1]))[::-1]
        return sum(1 for i in range(len(nums) - 1) if prefix[i] >= postfix[i + 1])

    # one pass O(n) / O(1)
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix, postfix = 0, sum(nums)

        count = 0
        for i in range(len(nums) - 1):
            prefix += nums[i]
            postfix -= nums[i]
            if prefix >= postfix:
                count += 1

        return count


solution = Solution()
assert solution.waysToSplitArray([10, 4, -8, 7]) == 2
assert solution.waysToSplitArray([2, 3, 1, 0]) == 2
assert solution.waysToSplitArray([0, 0]) == 1
