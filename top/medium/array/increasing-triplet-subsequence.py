from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


solution = Solution()
assert solution.increasingTriplet([1, 2, 3, 4, 5])
assert not solution.increasingTriplet([5, 4, 3, 2, 1])
assert solution.increasingTriplet([2, 1, 5, 0, 4, 6])
