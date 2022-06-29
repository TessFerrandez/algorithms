from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counts = defaultdict(int)

        # first window
        for num in nums[:k + 1]:
            if counts[num] == 1:
                return True
            counts[num] = 1

        # slide the window
        for i in range(k + 1, len(nums)):
            counts[nums[i - k - 1]] = 0
            if counts[nums[i]] == 1:
                return True
            counts[nums[i]] = 1

        return False


solution = Solution()
assert not solution.containsNearbyDuplicate([1, 2, 3], 3)
assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1)
assert not solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
