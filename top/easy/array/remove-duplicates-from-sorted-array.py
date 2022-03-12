from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        current = 0
        for next in range(1, n):
            if nums[next] != nums[current]:
                current += 1
                nums[current] = nums[next]

        return current + 1


solution = Solution()

arr = [1, 1, 2]
n = solution.removeDuplicates(arr)
assert arr[:n] == [1, 2]

arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
n = solution.removeDuplicates(arr)
assert arr[:n] == [0, 1, 2, 3, 4]
