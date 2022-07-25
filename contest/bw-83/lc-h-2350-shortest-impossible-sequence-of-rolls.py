from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # find full complete sets after one another
        # see how many complete sets we can find
        complete_found = 0
        found_set = set()

        for num in rolls:
            found_set.add(num)
            if len(found_set) == k:
                complete_found += 1
                found_set = set()

        return complete_found + 1


solution = Solution()
assert solution.shortestSequence([4,2,1,2,3,3,2,4,1], 4) == 3
assert solution.shortestSequence([1,1,2,2], 2) == 2
assert solution.shortestSequence([1,1,3,2,2,2,3,3], 4) == 1
