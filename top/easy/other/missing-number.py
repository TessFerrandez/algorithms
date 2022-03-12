from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = ((n + 1) * n) // 2
        missing = expected_sum
        for num in nums:
            missing -= num
        return missing


solution = Solution()
assert solution.missingNumber([3, 0, 1]) == 2
assert solution.missingNumber([0, 1]) == 2
assert solution.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
