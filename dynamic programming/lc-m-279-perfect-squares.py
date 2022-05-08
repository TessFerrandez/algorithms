from math import floor, sqrt
from collections import defaultdict


class Solution:
    # dp 1
    def numSquares1(self, n: int) -> int:
        if n <= 0:
            return 0

        dp = defaultdict(lambda: 10 ** 4)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        print(dp)
        return dp[n]

    # static dp
    def numSquares2(self, n: int) -> int:
        if n <= 0:
            return 0

        min_squares = [0]
        while len(min_squares) <= n:
            num, i, count_squares = len(min_squares), 1, 10 ** 4

            while i * i <= num:
                count_squares = min(count_squares, min_squares[num - i * i] + 1)
                i += 1

            min_squares.append(count_squares)

        return min_squares[n]

    # math
    def numSquares(self, n: int) -> int:
        '''
        Based on Lagranges Four Square Theorem there are only 4 possible solutions
        1, 2, 3, 4
        '''
        def is_square(n):
            sq = floor(sqrt(n))
            return sq * sq == n

        # 1 if is square
        if is_square(n):
            return 1

        # 4 if can be written as 4 ** (k * (8 * m) + 7)
        while (n & 3) == 0:     # n % 4 == 0
            n = n >> 2
        if (n & 7) == 7:        # n % 8 == 7
            return 4

        # 2 if 2 is the result
        sq = floor(sqrt(n))
        for i in range(1, sq + 1):
            if is_square(n - i * i):
                return 2

        # 3 otherwise
        return 3


solution = Solution()
assert solution.numSquares(12) == 3     # 4 + 4 + 4
assert solution.numSquares(13) == 2     # 4 + 9
