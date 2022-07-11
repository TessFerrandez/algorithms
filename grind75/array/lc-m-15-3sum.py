from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i, num in enumerate(nums):
            # skip duplicates
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result


solution = Solution()
assert solution.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert solution.threeSum([]) == []
assert solution.threeSum([0]) == []
