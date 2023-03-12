from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result


solution = Solution()
assert solution.xorBeauty([1, 4]) == 5
assert solution.xorBeauty([15,45,20,2,34,35,5,44,32,30]) == 34
