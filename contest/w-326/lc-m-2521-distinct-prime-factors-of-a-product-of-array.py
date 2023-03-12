from math import sqrt
from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()

        for num in nums:
            while num % 2 == 0:
                factors.add(2)
                num = num // 2

            for i in range(3, int(sqrt(num)) + 1, 2):
                while num % i == 0:
                    factors.add(i)
                    num = num // i

            if num > 2:
                factors.add(num)

        return len(factors)


solution = Solution()
assert solution.distinctPrimeFactors([27]) == 1
assert solution.distinctPrimeFactors([2,4,3,7,10,6]) == 4
assert solution.distinctPrimeFactors([2,4,8,16]) == 1
