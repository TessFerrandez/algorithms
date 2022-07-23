from functools import cache


class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        return 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))


solution = Solution()
assert solution.integerReplacement(8) == 3
assert solution.integerReplacement(7) == 4
assert solution.integerReplacement(4) == 2
