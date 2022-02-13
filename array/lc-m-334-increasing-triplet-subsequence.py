from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        post_big = [-1 for _ in range(len(nums))]
        pre_small = [-1 for _ in range(len(nums))]

        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                post_big[stack.pop()] = i
            stack.append(i)

        stack = []
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[j]:
                pre_small[stack.pop()] = j
            stack.append(j)

        for i in range(len(nums)):
            if pre_small[i] != -1 and post_big[i] != -1:
                return True

        return False


solution = Solution()
assert solution.increasingTriplet([1, 2, 3, 4, 5])
assert not solution.increasingTriplet([5, 4, 3, 2, 1])
assert solution.increasingTriplet([2, 1, 5, 0, 4, 6])
