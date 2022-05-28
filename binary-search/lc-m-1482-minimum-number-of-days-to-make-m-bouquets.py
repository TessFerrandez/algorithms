from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def is_valid(day):
            bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > day:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bouquets >= m

        if len(bloomDay) < m * k:
            return -1

        low, high = 1, max(bloomDay)
        while low < high:
            mid = low + (high - low) // 2
            if is_valid(mid):
                high = mid
            else:
                low = mid + 1

        return low


solution = Solution()
assert solution.minDays([1, 10, 3, 10, 2], 3, 1) == 3
assert solution.minDays([1, 10, 3, 10, 2], 3, 2) == -1
assert solution.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12
