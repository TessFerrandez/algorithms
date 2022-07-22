from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        def intersect(lst1, lst2):
            return [num for num in lst2 if num in lst1]

        result = set(nums[0])
        for arr in nums[1:]:
            result = intersect(result, arr)
        return sorted(list(result))


solution = Solution()
assert solution.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]) == [3, 4]
assert solution.intersection([[1, 2, 3],[4, 5, 6]]) == []
