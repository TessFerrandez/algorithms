class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num):
            count = 0
            for val in range(1, m + 1):
                add = min(num // val, n)
                if add == 0:
                    # early exit
                    break
                count += add
            return count >= k

        low, high = 1, n * m

        while low < high:
            mid = (low + high) // 2
            if enough(mid):
                high = mid
            else:
                low = mid + 1
        return low


solution = Solution()
assert solution.findKthNumber(3, 3, 5) == 3
assert solution.findKthNumber(2, 3, 6) == 6
