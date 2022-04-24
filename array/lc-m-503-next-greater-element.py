from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(n * 2 - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            result[i % n] = -1 if not stack else nums[stack[-1]]
            stack.append(i % n)

        return result


solution = Solution()
assert solution.nextGreaterElements([1, 2, 1]) == [2, -1, 2]
assert solution.nextGreaterElements([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
