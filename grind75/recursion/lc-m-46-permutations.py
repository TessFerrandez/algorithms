from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        results = []

        for i in range(len(nums)):
            for sub_result in self.permute(nums[:i] + nums[i + 1:]):
                results.append([nums[i]] + sub_result)

        return results


solution = Solution()
assert solution.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
assert solution.permute([0, 1]) == [[0, 1], [1, 0]]
assert solution.permute([1]) == [[1]]
