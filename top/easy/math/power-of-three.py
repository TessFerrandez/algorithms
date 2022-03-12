import numpy as np


class Solution:
    def isPowerOfThree1(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        three_str = np.base_repr(n, 3)
        return three_str.count('1') == 1 and three_str.count('2') == 0


solution = Solution()
assert solution.isPowerOfThree(27)
assert not solution.isPowerOfThree(0)
assert solution.isPowerOfThree(9)
