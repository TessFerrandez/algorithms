from itertools import combinations
from typing import List


class Solution:
    def combinationSum3_1(self, k: int, n: int) -> List[List[int]]:
        def dfs(nums, k, n, path, result):
            if k < 0 or n < 0:
                return None
            if k == 0 and n == 0:
                result.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1:], k - 1, n - nums[i], path + [nums[i]], result)

        result = []
        dfs(list(range(1, 10)), k, n, [], result)
        return result

    def combinationSum3_2(self, k: int, n: int) -> List[List[int]]:
        def dfs(i, k, n, path, result):
            if k < 0 or n < 0:
                return None
            if k == 0 and n == 0:
                result.append(path)
            for num in range(i, 10):
                dfs(num + 1, k - 1, n - num, path + [num], result)

        result = []
        dfs(1, k, n, [], result)
        return result

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(combo) for combo in combinations(range(1, 10), k) if sum(combo) == n]


solution = Solution()
assert solution.combinationSum3(3, 7) == [[1, 2, 4]]
assert solution.combinationSum3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]]
assert solution.combinationSum3(4, 1) == []
