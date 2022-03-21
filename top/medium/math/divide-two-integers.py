class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            current_divisor, num_divisors = divisor, 1

            while dividend >= current_divisor:
                dividend -= current_divisor
                result += num_divisors

                num_divisors += num_divisors
                current_divisor += current_divisor

        result = result if positive else -result
        return min(max(-2 ** 31, result), 2 ** 31 - 1)


solution = Solution()
assert solution.divide(6, 3) == 2
assert solution.divide(10, 3) == 3
assert solution.divide(7, -3) == -2
