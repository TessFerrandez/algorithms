class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n

        while low <= high:
            mid = (high + low) // 2
            mid_sum = mid * (mid + 1) // 2
            if mid_sum == n:
                return mid
            if n < mid_sum:
                high = mid - 1
            else:
                low = mid + 1
        return high


solution = Solution()
assert solution.arrangeCoins(5) == 2
assert solution.arrangeCoins(8) == 3
