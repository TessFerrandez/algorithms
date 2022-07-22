from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        total = 0
        counts = Counter(tasks)
        for count in counts:
            c = counts[count]
            if c == 1:
                return -1
            if c % 3 == 0:
                total += c // 3
            else:
                total += c // 3 + 1

        return total


solution = Solution()
assert solution.minimumRounds([2,2,3,3,2,4,4,4,4,4]) == 4
assert solution.minimumRounds([2,3,3]) == -1
