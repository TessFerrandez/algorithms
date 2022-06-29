from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, total_sum = 0, sum(nums)
        for i in range(len(nums)):
            if l_sum == total_sum - l_sum - nums[i]:
                return i
            l_sum += nums[i]
        return -1


solution = Solution()
assert solution.pivotIndex([1,7,3,6,5,6]) == 3
assert solution.pivotIndex([1,2,3]) == -1
assert solution.pivotIndex([2,1,-1]) == 0
assert solution.pivotIndex([-1, -1, 0, 1, 1, 0]) == 5
