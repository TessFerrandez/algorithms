from math import floor, sqrt
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num == 1:
                return False
            for divisor in range(2, floor(sqrt(num)) + 1):
                if num % divisor == 0:
                    return False
            return True

        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]  # twin or [2, 3]
                primes.append(candidate)

        gaps = ([primes[i - 1], primes[i]] for i in range(1, len(primes)))

        return min(gaps, key=lambda gap: (gap[1] - gap[0], gap[0]), default=[-1, -1])


solution = Solution()
assert solution.closestPrimes(19, 31) == [29, 31]
assert solution.closestPrimes(10, 19) == [11, 13]
assert solution.closestPrimes(4, 6) == [-1, -1]
