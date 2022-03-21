class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True

        if n < 10:
            return False

        digits = str(n)
        digit_sum = sum(int(digit) ** 2 for digit in digits)
        return self.isHappy(digit_sum)


solution = Solution()
assert solution.isHappy(19)
assert not solution.isHappy(2)
