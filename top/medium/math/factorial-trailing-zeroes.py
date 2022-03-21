class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)


solution = Solution()
assert solution.trailingZeroes(30) == 7
assert solution.trailingZeroes(3) == 0
assert solution.trailingZeroes(5) == 1
assert solution.trailingZeroes(0) == 0
