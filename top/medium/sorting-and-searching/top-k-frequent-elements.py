from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [n[0] for n in counts.most_common(k)]


solution = Solution()
assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert solution.topKFrequent([1], 1) == [1]
