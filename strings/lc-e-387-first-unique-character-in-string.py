class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1


solution = Solution()
assert solution.firstUniqChar('leetcode') == 0
assert solution.firstUniqChar('loveleetcode') == 2
assert solution.firstUniqChar('aabb') == -1
