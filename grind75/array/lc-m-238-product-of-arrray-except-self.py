from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]

        product = 1
        for num in nums:
            product *= num
            prefix.append(product)

        product = 1
        results = []
        for i in range(len(nums) - 1, -1, -1):
            results.append(prefix[i] * product)
            product *= nums[i]

        return results[:: -1]


solution = Solution()
assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
