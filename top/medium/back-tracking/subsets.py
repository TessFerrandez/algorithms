from typing import List


class Solution:
    # cascading
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]

        for num in nums:
            new_subset = []

            for sub in subset:
                new_subset.append(sub + [num])

            subset += new_subset

        return subset

    # backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, current=[]):
            if len(current) == k:
                result.append(current[:])
                return

            for i in range(first, n):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        result = []
        n = len(nums)

        for k in range(n + 1):
            backtrack()

        return result


solution = Solution()
assert solution.subsets([1, 2, 3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
# assert solution.subsets([1, 2, 3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert solution.subsets([0]) == [[], [0]]
