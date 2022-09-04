from math import sqrt, floor
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for w in range(floor(sqrt(area)), 0, -1):
            if area % w == 0:
                return [area // w, w]

        return []


solution = Solution()
assert solution.constructRectangle(4) == [2, 2]
assert solution.constructRectangle(37) == [37, 1]
assert solution.constructRectangle(122122) == [427, 286]
