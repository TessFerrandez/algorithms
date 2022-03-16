from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            for permutation in self.permute(nums[: i] + nums[i + 1:]):
                result.append([nums[i]] + permutation)

        return result


solution = Solution()
assert solution.permute([1, 2, 3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
assert solution.permute([0, 1]) == [[0, 1], [1, 0]]
assert solution.permute([1]) == [[1]]
