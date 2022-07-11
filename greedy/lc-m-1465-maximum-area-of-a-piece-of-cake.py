from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts.sort()
        verticalCuts = [0] + verticalCuts + [w]

        max_height = max(horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts)))
        max_width = max(verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts)))

        return (max_height * max_width) % ((10 ** 9) + 7)


solution = Solution()
assert solution.maxArea(5, 4, [1, 2, 4], [1, 3]) == 4
assert solution.maxArea(5, 4, [3, 1], [1]) == 6
assert solution.maxArea(5, 4, [3], [3]) == 9
assert solution.maxArea(1000000000, 1000000000, [2], [2]) == 81
