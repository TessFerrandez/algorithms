from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        # are there at least k - 1 pairs with a distance smaller than this?
        def enough(distance):
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1  # count pairs
                i += 1
            return count >= k

        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if enough(mid):
                high = mid
            else:
                low = mid + 1
        return low


solution = Solution()
assert solution.smallestDistancePair([1, 3, 1], 1) == 0
assert solution.smallestDistancePair([1, 1, 1], 2) == 0
assert solution.smallestDistancePair([1, 6, 1], 3) == 5
