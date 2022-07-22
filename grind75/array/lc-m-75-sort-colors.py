from typing import Counter, List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = Counter(nums)
        i = 0
        for n in range(3):
            for _ in range(counts[n]):
                nums[i] = n
                i += 1

        return nums


solution = Solution()
assert solution.sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
assert solution.sortColors([2,0,1]) == [0, 1, 2]
