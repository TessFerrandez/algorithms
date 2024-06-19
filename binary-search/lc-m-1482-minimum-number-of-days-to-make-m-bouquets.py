from typing import List


class Solution:
    def is_valid(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        bouquets, flowers = 0, 0
        for bloom in bloomDay:
            if bloom > day:
                flowers = 0
            else:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
        return bouquets >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        start = 0
        end = max(bloomDay)

        while start < end:
            mid = start + (end - start) // 2
            if self.is_valid(bloomDay, m, k, mid):
                end = mid
            else:
                start = mid + 1

        return start


solution = Solution()
assert solution.minDays([1, 10, 3, 10, 2], 3, 1) == 3
assert solution.minDays([1, 10, 3, 10, 2], 3, 2) == -1
assert solution.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12
