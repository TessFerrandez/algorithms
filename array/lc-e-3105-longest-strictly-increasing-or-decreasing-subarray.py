from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestIncreasing = 1
        longestDecreasing = 1

        increasing = 1
        decreasing = 1
        current = nums[0]

        for num in nums[1:]:
            if num > current:
                increasing += 1
                decreasing = 1
            elif num < current:
                decreasing += 1
                increasing = 1
            else:
                increasing = 1
                decreasing = 1

            longestIncreasing = max(longestIncreasing, increasing)
            longestDecreasing = max(longestDecreasing, decreasing)

            current = num

        return max(longestIncreasing, longestDecreasing)


solution = Solution()
assert solution.longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2
assert solution.longestMonotonicSubarray([3, 3, 3, 3]) == 1