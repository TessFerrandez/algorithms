class Solution:
    def isUgly(self, n: int) -> bool:
        for prime in 2, 3, 5:
            while n > 0 and n % prime == 0:
                n /= prime
        return n == 1


solution = Solution()
assert solution.isUgly(6)
assert solution.isUgly(1)
assert not solution.isUgly(14)
