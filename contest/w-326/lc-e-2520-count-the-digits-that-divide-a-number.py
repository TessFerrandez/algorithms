class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(d) for d in list(str(num))]
        return sum(1 for digit in digits if num % digit == 0)


solution = Solution()
assert solution.countDigits(7) == 1
assert solution.countDigits(121) == 2
assert solution.countDigits(1248) == 4
