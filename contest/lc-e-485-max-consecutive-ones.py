from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        consecutive = 0

        for num in nums:
            if num == 1:
                consecutive += 1
            else:
                max_consecutive = max(max_consecutive, consecutive)
                consecutive = 0

        max_consecutive = max(max_consecutive, consecutive)
        return max_consecutive


solution = Solution()
assert solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
assert solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
