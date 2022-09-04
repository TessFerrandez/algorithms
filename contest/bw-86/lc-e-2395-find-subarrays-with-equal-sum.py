from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i in range(len(nums) - 1):
            the_sum = nums[i] + nums[i + 1]
            if the_sum in sums:
                return True
            sums.add(the_sum)

        return False


solution = Solution()
assert solution.findSubarrays([4,2,4])
assert not solution.findSubarrays([1,2,3,4,5])
assert solution.findSubarrays([0,0,0])
