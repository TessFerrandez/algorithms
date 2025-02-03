# array, sorting, counting sort
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        # add an extra 0 to the end of the list to avoid index out of range
        citations.append(0)
        for i, citation in enumerate(citations):
            if i >= citation:
                return i
        return 0


solution = Solution()
assert(solution.hIndex([3, 0, 6, 1, 5]) == 3)
assert(solution.hIndex([1, 3, 1]) == 1)
