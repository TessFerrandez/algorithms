from collections import Counter, defaultdict
from typing import List
from heapq import nlargest


class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        counts_hash = defaultdict(int)

        for num in nums:
            counts_hash[num] += 1

        counts = [(counts_hash[count], count) for count in counts_hash]
        counts.sort(reverse=True)
        return [num[1] for num in counts[:k]]

    # with builtins
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return nlargest(k, counter.keys(), counter.get)

    # with builtins
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num[0] for num in counter.most_common(k)]


solution = Solution()
assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert solution.topKFrequent([1], 1) == [1]
