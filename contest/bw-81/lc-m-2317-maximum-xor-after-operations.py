from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result |= num
        return result


solution = Solution()
assert solution.maximumXOR([3, 2, 4, 6]) == 7

# 011
# 010
# 100
# 110
# ------
# 231 <- evens can be reduced, and odds can be kept => 111 = 7

assert solution.maximumXOR([1, 2, 3, 9, 2]) == 11

# 0001
# 0010
# 0011
# 1001
# 0010
# -----
# 1023 => 1011 = 11
