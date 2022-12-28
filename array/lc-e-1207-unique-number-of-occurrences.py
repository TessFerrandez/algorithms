from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = list(Counter(arr).values())
        count_of_counts = Counter(counts)
        for count in count_of_counts:
            if count_of_counts[count] != 1:
                return False
        return True


solution = Solution()
assert solution.uniqueOccurrences([1, 2, 2, 1, 1, 3])
assert not solution.uniqueOccurrences([1, 2])
assert solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
