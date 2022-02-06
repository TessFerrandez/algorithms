from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        count = 0
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                count += 1
            else:
                more.append(num)

        for i in range(count):
            less.append(pivot)

        return less + more


solution = Solution()
assert solution.pivotArray([9, 12, 5, 10, 14, 3, 10], 10) == [9, 5, 3, 10, 10, 12, 14]
assert solution.pivotArray([-3, 4, 3, 2], 2) == [-3, 2, 4, 3]
