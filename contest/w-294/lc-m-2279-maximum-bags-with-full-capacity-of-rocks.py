from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        missing = [capacity[i] - rocks[i] for i in range(len(capacity))]
        missing.sort()

        count = 0
        for n in missing:
            if n <= additionalRocks:
                count += 1
                additionalRocks -= n
            else:
                break

        return count


solution = Solution()
assert solution.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2) == 3
assert solution.maximumBags([10, 2, 2], [2, 2, 0], 100) == 3
