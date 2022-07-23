from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        prev = best = sum(i * nums[i] for i in range(n))
        num_sum = sum(nums)

        for i in range(1, n):
            prev = prev + num_sum - n * nums[n - i]
            best = max(best, prev)

        return best


solution = Solution()
assert solution.maxRotateFunction([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 330
assert solution.maxRotateFunction([4, 3, 2, 6]) == 26
assert solution.maxRotateFunction([100]) == 0
