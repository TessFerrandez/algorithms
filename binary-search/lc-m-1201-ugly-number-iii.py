from math import gcd


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def enough(num) -> bool:
            total = num // a + num // b + num // c - num // ab - num // ac - num // bc + num // abc
            return total >= n

        ab = a * b // gcd(a, b)
        ac = a * c // gcd(a, c)
        bc = b * c // gcd(b, c)
        abc = a * bc // gcd(a, bc)

        low, high = 1, 10 ** 10
        while low < high:
            mid = (low + high) // 2
            if enough(mid):
                high = mid
            else:
                low = mid + 1
        return low


solution = Solution()
assert solution.nthUglyNumber(3, 2, 3, 5) == 4
assert solution.nthUglyNumber(4, 2, 3, 4) == 6
assert solution.nthUglyNumber(5, 2, 11, 13) == 10
