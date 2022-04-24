from math import sqrt


class Solution:
    # brute force
    def judgeSquareSum1(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            for b in range(int(sqrt(c)) + 1):
                if a * a + b * b == c:
                    return True
        return False

    # better brute force
    def judgeSquareSum2(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = c - (a * a)
            i = 1
            sum = 0
            while sum < b:
                sum += i
                i += 2
            if sum == b:
                return True
        return False

    # using sqrt
    def judgeSquareSum3(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a * a)
            if b == int(b):
                return True
        return False

    # using binary search
    def judgeSquareSum4(self, c: int) -> bool:
        def is_square(start, end, n):
            if start > end:
                return False
            mid = (start + end) // 2
            if mid * mid == n:
                return True
            if mid * mid > n:
                return is_square(start, mid - 1, n)
            return is_square(mid + 1, end, n)

        for a in range(int(sqrt(c)) + 1):
            b = c - a * a
            if is_square(0, b, b):
                return True
        return False

    # fermats theorem
    def judgeSquareSum(self, c: int) -> bool:
        '''
        any positive number c can be expressed as the sum
        of 2 squares, if and only if in the prime factorization of c
        every prime on the form 4k + 3 occurs and even number of times
        '''
        for i in range(2, int(sqrt(c)) + 1):
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c /= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
        return c % 4 != 3


solution = Solution()
assert solution.judgeSquareSum(5)
assert not solution.judgeSquareSum(3)
