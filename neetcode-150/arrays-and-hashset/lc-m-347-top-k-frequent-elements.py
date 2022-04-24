from collections import defaultdict
from typing import List


# Time: O(n log n) - due to the sort
# Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        frequencies = [(count, num) for num, count in counts.items()]
        frequencies.sort(reverse=True)
        return [freq[1] for freq in frequencies[:k]]


solution = Solution()
assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert solution.topKFrequent([1], 1) == [1]
