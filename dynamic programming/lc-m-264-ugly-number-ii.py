'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors, k = [2, 3, 5], 3
        starts, numbers = [0, 0, 0], [1]

        for _ in range(n - 1):
            candidates = [factors[i] * numbers[starts[i]] for i in range(k)]
            new_num = min(candidates)
            numbers.append(new_num)
            starts = [starts[i] + (candidates[i] == new_num) for i in range(k)]

        return numbers[-1]


solution = Solution()
assert solution.nthUglyNumber(11) == 15
assert solution.nthUglyNumber(10) == 12
assert solution.nthUglyNumber(1) == 1
