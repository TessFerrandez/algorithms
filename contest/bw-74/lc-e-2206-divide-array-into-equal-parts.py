from typing import Counter, List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for count in counts.values():
            if count % 2 != 0:
                return False
        return True


solution = Solution()
assert solution.divideArray([3, 2, 3, 2, 2, 2])
assert not solution.divideArray([1, 2, 3, 4])
