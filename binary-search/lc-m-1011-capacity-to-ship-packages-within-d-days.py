from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(capacity):
            current_days, current_total = 1, 0

            for weight in weights:
                current_total += weight
                if current_total > capacity:
                    current_total = weight
                    current_days += 1
                    if current_days > days:
                        return False

            return True

        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2

            if is_valid(mid):
                high = mid
            else:
                low = mid + 1

        return low


solution = Solution()
assert solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5) == 15
assert solution.shipWithinDays([3,2,2,4,1,4], 3) == 6
assert solution.shipWithinDays([1,2,3,1,1], 4) == 3
