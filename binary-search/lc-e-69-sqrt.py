class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        low, high = 0, x

        while low < high:
            mid = (low + high) // 2

            if mid * mid > x:
                high = mid
            else:
                low = mid + 1

        return low - 1


solution = Solution()
assert solution.mySqrt(0) == 0
assert solution.mySqrt(4) == 2
assert solution.mySqrt(8) == 2
