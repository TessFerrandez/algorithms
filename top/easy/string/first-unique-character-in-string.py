from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i

        return -1


solution = Solution()
assert solution.firstUniqChar('leetcode') == 0
assert solution.firstUniqChar('loveleetcode') == 2
assert solution.firstUniqChar('aabb') == -1
