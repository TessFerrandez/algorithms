from typing import List


class Solution:
    def longestOnes1(self, nums: List[int], k: int) -> int:
        left = 0

        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1

        return right - left + 1

    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        zeros, max_len = 0, 0

        while right < len(nums):
            # expand until we are invalid
            if (nums[right] == 0 and zeros < k) or (nums[right] == 1 and zeros <= k):
                zeros += 1 if nums[right] == 0 else 0
                right += 1
                max_len = max(max_len, right - left)
            # shrink til we are valid
            else:
                zeros -= nums[left] == 0
                left += 1

        return max_len


solution = Solution()
assert solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
assert solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
