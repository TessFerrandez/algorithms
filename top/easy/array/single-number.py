from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result


solution = Solution()
assert solution.singleNumber([2, 2, 1]) == 1
assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
assert solution.singleNumber([1]) == 1
