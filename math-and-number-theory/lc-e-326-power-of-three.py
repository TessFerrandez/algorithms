class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        if n == 1:
            return True

        if n % 3 != 0:
            return False

        return self.isPowerOfThree(n // 3)


solution = Solution()
assert solution.isPowerOfThree(27) == True
assert solution.isPowerOfThree(0) == False
assert solution.isPowerOfThree(9) == True
assert solution.isPowerOfThree(6) == False
