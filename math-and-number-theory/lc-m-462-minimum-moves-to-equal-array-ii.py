from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)


solution = Solution()
assert solution.minMoves2([1, 2, 3]) == 2
assert solution.minMoves2([1, 10, 2, 9]) == 16
assert solution.minMoves2([1, 2, 3, 10]) == 10
