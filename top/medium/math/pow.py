class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / x * self.myPow(1 / x, -(n + 1))

        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)


solution = Solution()
assert solution.myPow(2, 10) == 1024
assert solution.myPow(2.1, 3) == 9.261000000000001
assert solution.myPow(2, -2) == 0.25
