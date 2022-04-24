from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]

        # product of all the numbers to the left of i
        for i in range(len(nums) - 1):
            result.append(nums[i] * result[-1])

        postfix_product = 1
        # multiply with product of all the numbers to the right of i
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result


solution = Solution()
assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
