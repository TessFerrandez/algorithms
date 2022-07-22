from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        max_steps = 0
        nums = nums[::-1]
        stack = [(nums[0], 0)]

        for i in range(1, len(nums)):
            steps = 0
            while stack and stack[-1][0] < nums[i]:
                steps = max(steps + 1, stack[-1][1])
                stack.pop()
            stack.append((nums[i], steps))
            max_steps = max(max_steps, steps)
        return max_steps


solution = Solution()
assert solution.totalSteps([7, 14, 4, 14, 13, 2, 6, 13]) == 3
assert solution.totalSteps([5, 3, 4, 3, 7, 3, 6, 11, 8, 5, 11]) == 2
assert solution.totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]) == 3
assert solution.totalSteps([4, 5, 7, 7, 13]) == 0
