from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = {}

        for i, ch in enumerate(s):
            if ch in seen:
                if i - seen[ch] - 1 != distance[ord(ch) - ord('a')]:
                    return False
            seen[ch] = i

        return True


solution = Solution()
assert solution.checkDistances(s="abaccb", distance=[1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
assert not solution.checkDistances(s="aa", distance=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
