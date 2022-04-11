from typing import List


class Solution:
    # my solution
    def maximumCandies1(self, candies: List[int], k: int) -> int:
        def can_do(pile_size):
            if pile_size == 0:
                return True
            if sum(pile // pile_size for pile in candies) >= k:
                return True
            return False

        total = sum(candies)
        low, high = 0, total // k

        while low <= high:
            mid = (low + high) // 2
            if can_do(mid):
                if can_do(mid + 1):
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1
        return low

    # cleaner
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low, high = 0, sum(candies) // k

        while low < high:
            mid = (low + high + 1) // 2
            if k > sum(pile // mid for pile in candies):
                high = mid - 1
            else:
                low = mid

        return low


solution = Solution()
assert solution.maximumCandies([1, 2, 3, 4, 10], 5) == 3
assert solution.maximumCandies([5, 8, 6], 3) == 5
assert solution.maximumCandies([2, 5], 11) == 0
