from typing import List
from UnionFind import UnionFind


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)
        visited = set()
        num = set(nums)

        for num in nums:
            if num - 1 in visited:
                uf.union(num, num - 1)
            if num + 1 in visited:
                uf.union(num, num + 1)
            visited.add(num)

        return uf.largest_component_size()


solution = Solution()
assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
