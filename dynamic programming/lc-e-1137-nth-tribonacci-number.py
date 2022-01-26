'''
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        prev0, prev1, prev2 = 0, 1, 1
        result = 0
        for _ in range(3, n + 1):
            result = prev0 + prev1 + prev2
            prev0, prev1, prev2 = prev1, prev2, result

        return result


solution = Solution()
assert solution.tribonacci(4) == 4
assert solution.tribonacci(25) == 1389537
