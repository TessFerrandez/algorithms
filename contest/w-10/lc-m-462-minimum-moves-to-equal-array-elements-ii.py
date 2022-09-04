from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)

        def find_median():
            return nums[len(nums) // 2]

        median = find_median()
        return sum(abs(num - median) for num in nums)


solution = Solution()
assert solution.minMoves2([1, 2, 3]) == 2
assert solution.minMoves2([1, 10, 2, 9]) == 16
