from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            additional = []
            for subset in result:
                additional.append(subset + [num])
            result += additional

        return result


solution = Solution()
assert solution.subsets([1, 2, 3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert solution.subsets([0]) == [[], [0]]
