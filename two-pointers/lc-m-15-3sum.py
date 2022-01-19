from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        num_len = len(nums)
        combos = []

        for i in range(num_len):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            start, end = i + 1, num_len - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    combos.append([nums[i], nums[start], nums[end]])
                    start += 1
                    # skip duplicates
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1

        return combos


solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
