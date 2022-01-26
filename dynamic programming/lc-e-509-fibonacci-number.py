'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev0, prev1 = 0, 1
        result = 0
        for _ in range(2, n + 1):
            result = prev0 + prev1
            prev0, prev1 = prev1, result

        return result


solution = Solution()
assert solution.fib(2) == 1
assert solution.fib(3) == 2
assert solution.fib(4) == 3
