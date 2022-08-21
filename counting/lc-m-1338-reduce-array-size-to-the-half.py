from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr).most_common()
        half = len(arr) // 2

        removed_nums, removed_count = 0, 0
        for _, count in counts:
            removed_nums += 1
            removed_count += count
            if removed_count >= half:
                break

        return removed_nums


solution = Solution()
assert solution.minSetSize([3,3,3,3,5,5,5,2,2,7]) == 2
assert solution.minSetSize([7,7,7,7,7,7]) == 1
