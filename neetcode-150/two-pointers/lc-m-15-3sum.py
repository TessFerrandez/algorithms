from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                # avoid duplicates
                continue

            left, right = i + 1, n - 1
            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    # found it
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result


solution = Solution()
assert solution.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert solution.threeSum([]) == []
assert solution.threeSum([0]) == []
