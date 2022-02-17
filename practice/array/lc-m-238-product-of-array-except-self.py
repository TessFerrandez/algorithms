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
