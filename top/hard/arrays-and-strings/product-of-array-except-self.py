from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        prefix_product = 1
        for num in nums[:-1]:
            prefix_product *= num
            result.append(prefix_product)

        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result


solution = Solution()
assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
