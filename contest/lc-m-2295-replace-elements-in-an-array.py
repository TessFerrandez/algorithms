from typing import List


class Solution:
    # my solution
    def arrayChange1(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        number_map = {}
        number_map_rev = {}

        for fr, to in operations:
            if fr in number_map_rev:
                prev = number_map_rev[fr]
                number_map[prev] = to
                del(number_map_rev[fr])
                number_map_rev[to] = prev
            else:
                number_map[fr] = to
                number_map_rev[to] = fr

        indices = []
        for i, num in enumerate(nums):
            if num in number_map:
                indices.append(i)

        for i in indices:
            nums[i] = number_map[nums[i]]

        return nums

    # cleaned up
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        replacements = {}

        for fr, to in reversed(operations):
            replacements[fr] = replacements.get(to, to)
        for i, num in enumerate(nums):
            if num in replacements:
                nums[i] = replacements[num]
        return nums


solution = Solution()
assert solution.arrayChange([1, 2], [[1, 3], [2, 1], [3, 2]]) == [2, 1]
assert solution.arrayChange([1,2,4,6], [[1,3],[4,7],[6,1]]) == [3, 2, 7, 1]
