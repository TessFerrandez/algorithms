from math import sqrt


class Solution:
    # brute force
    def arrangeCoins1(self, n: int) -> int:
        if n <= 2:
            return 1

        total = 0
        for i in range(n):
            total += i
            if total >= n:
                if total == n:
                    return i
                return i - 1

    # binary search
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1
        if n == 3:
            return 2

        low, high = 2, n // 2
        while low <= high:
            mid = (low + high) // 2
            coins_filled = mid * (mid + 1) // 2

            if coins_filled == n:
                return mid
            if coins_filled < n:
                low = mid + 1
            else:
                high = mid - 1

        return high

    # using math
    def arrangeCoins2(self, n: int) -> int:
        return int((sqrt(8 * n + 1) - 1) / 2)


solution = Solution()
assert solution.arrangeCoins(1) == 1
assert solution.arrangeCoins(2) == 1
assert solution.arrangeCoins(5) == 2
assert solution.arrangeCoins(8) == 3
