from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix_sum = list(accumulate(sorted(nums)))
        return [bisect_right(prefix_sum, query) for query in queries]


solution = Solution()
assert solution.answerQueries([4,5,2,1], [3,10,21]) == [2, 3, 4]
assert solution.answerQueries([2, 3, 4, 5], [1]) == [0]
