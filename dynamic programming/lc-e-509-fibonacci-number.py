'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''
from functools import cache


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev0, prev1 = 0, 1
        result = 0
        for _ in range(2, n + 1):
            result = prev0 + prev1
            prev0, prev1 = prev1, result

        return result

    def fib2(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    @cache
    def fib3(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib4(self, n):
        fibs = [0, 1]

        for i in range(2, n + 1):
            fibs.append(fibs[i - 1] + fibs[i - 2])

        return fibs[n]


solution = Solution()
assert solution.fib(2) == 1
assert solution.fib(3) == 2
assert solution.fib(4) == 3
