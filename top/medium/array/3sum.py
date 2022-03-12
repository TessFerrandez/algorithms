from collections import Counter
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        unique = set(nums)

        combos = set()
        for num in unique:
            counts[num] -= 1
            if counts[num] == 0:
                del counts[num]

            for n2 in counts:
                target = 0 - num - n2
                if target in counts:
                    if target == n2 and counts[target] < 2:
                        continue
                    combos.add(tuple(sorted([num, n2, target])))

            del counts[num]

        return [list(combo) for combo in combos]


solution = Solution()
assert solution.threeSum([0, 0]) == []
assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
assert solution.threeSum([]) == []
assert solution.threeSum([0]) == []
