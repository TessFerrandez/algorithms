class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        low, high = 1, x

        while low < high - 1:
            mid = (low + high) // 2
            if x / mid >= mid:
                low = mid
            else:
                high = mid - 1

        if x / high >= high:
            return high
        return low


solution = Solution()
assert solution.mySqrt(4) == 2
assert solution.mySqrt(8) == 2
