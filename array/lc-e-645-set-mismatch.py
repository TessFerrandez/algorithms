from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = set()

        duplicate = 0

        for number in nums:
            if number in visited:
                duplicate = number
            visited.add(number)

        for number in range(1, len(nums) + 1):
            if number not in visited:
                return [duplicate, number]


solution = Solution()
assert solution.findErrorNums([1, 2, 2, 4]) == [2, 3]
assert solution.findErrorNums([1, 1]) == [1, 2]
