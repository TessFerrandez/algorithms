# two pointers, string, dynamic programming
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        while s and t:
            if s[0] == t[0]:
                s = s[1:]
            t = t[1:]

        return not s


solution = Solution()
assert solution.isSubsequence("abc", "ahbgdc")
assert not solution.isSubsequence("axc", "ahbgdc")
