from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for i in range(1, numRows):
            triangle.append([1])
            for j in range(i - 1):
                triangle[-1].append(triangle[-2][j] + triangle[-2][j + 1])
            triangle[-1].append(1)

        return triangle


solution = Solution()
assert solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert solution.generate(1) == [[1]]
