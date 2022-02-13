'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        pre = 1
        for num in nums:
            pre *= num
            prefix.append(pre)

        post = 1
        for num in nums[::-1]:
            post *= num
            postfix.append(post)

        prefix = [1] + prefix
        postfix = postfix[::-1] + [1]

        return [prefix[i] * postfix[i + 1] for i in range(len(nums))]


solution = Solution()
assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
