from collections import defaultdict
from math import ceil, sqrt


class Solution:
    # TLE?
    def countPrimes2(self, n: int) -> int:
        is_prime = defaultdict(lambda: True)

        i = 2
        while i * i <= n:
            if not is_prime[i]:
                continue

            for j in range(i * i, n, i):
                is_prime[j] = False

            i += 1

        return sum(1 for i in range(2, n) if is_prime[i])

    def countPrimes(self, n: int) -> int:
        is_prime = [True for _ in range(n + 1)]

        for i in range(2, ceil(sqrt(n)) + 1):
            if not is_prime[i]:
                continue
            for j in range(i * i, n, i):
                is_prime[j] = False

        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1

        return count


solution = Solution()
assert solution.countPrimes(0) == 0
assert solution.countPrimes(1) == 0
assert solution.countPrimes(10) == 4
